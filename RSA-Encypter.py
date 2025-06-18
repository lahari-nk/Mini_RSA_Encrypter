import random
import math

def check_prime(num):
    if num<=1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True

def generate_prime():
    while True:
        num=random.randint(1000000,9999999) #In actual RSA System there will be 31 digit primes byt for the sake of processing we will use smaller numbers
        if check_prime(num):
            return num

def generate_public_key(phi_n):
    while True:
        e=random.randint(2,phi_n-1)
        if math.gcd(e,phi_n)==1:
            return e

def generate_private_key(e,phi_n):
    return pow(e,-1,phi_n)

def encoding(message):
    m=0
    for char in message:
        m=m*256+ord(char)
    return m

def decoding(m):
    message=""
    while m>0:
        message=chr(m%256)+message
        m//=256
    return message

def encryption(m,e,n):
    return pow(m,e,n)

def decryption(c,d,n):
    return pow(c,d,n)

choice=input("Enter 'e' for encryption or 'd' for decryption: ").strip().lower()

if choice=="e":
    message=input("Enter your message to encrypt: ")
    
    p=generate_prime()
    q=generate_prime()
    n=p*q
    phi_n=(p-1)*(q-1)
    e=generate_public_key(phi_n)
    d=generate_private_key(e, phi_n)

    m=encoding(message)
    
    if m>=n:
        print("Error: Message is too long. Try shorter input.")
    else:
        c=encryption(m, e, n)
        print("\nEncrypted Message:", c)
        print("Private Key:", d)
        print("Public Key:", n)

elif choice=="d":
    try:
        c=int(input("Enter encrypted message: "))
        d=int(input("Enter private key: "))
        n=int(input("Enter public code: "))
        
        m=decryption(c, d, n)
        message=decoding(m)
        print("\nDecrypted Message:", message)
    except:
        print("Invalid input or decryption failed.")

else:
    print("Invalid choice. Use 'e' or 'd'.")