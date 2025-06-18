# Mini_RSA_Encrypter

This project is a simple yet powerful implementation of the RSA encryption algorithm written entirely from scratch using only basic Python and math/random libraries.

## Features

- Generates large random prime numbers
- Creates public and private RSA keys
- Converts messages to integers using base-256 encoding
- Performs modular exponentiation for encryption and decryption
- Supports custom messages and prints encrypted/decrypted results

## How It Works

1. Encryption Mode
   - User inputs a plaintext message (like "HELLO").
   - Program generates two large prime numbers p and q.
   - Calculates n = p × q and Euler’s totient ϕ(n) = (p−1)(q−1).
   - Picks public key e such that gcd(e, ϕ(n)) = 1.
   - Calculates private key d ≡ e⁻¹ mod ϕ(n).
   - Encodes message into an integer m.
   - Encrypts using c = m^e mod n.

2. Decryption Mode
   - User enters the encrypted message c, private key d, and public key n.
   - Computes original message integer m = c^d mod n.
   - Decodes m back into the plaintext string.

##  Getting Started

Requirements
- Python 3.8+

You’ll be prompted to choose between encryption or decryption.

### 🔒 Encryption Example

Enter 'e' for encryption or 'd' for decryption: e
Enter your message to encrypt: HELLO

Encrypted Message: 279023849382023
Private Key: 94828482938
Public Key: 23423442323

### 🔓 Decryption Example

Enter 'e' for encryption or 'd' for decryption: d
Enter encrypted message: 279023849382023
Enter private key: 23423442323
Enter public key: 94828482938

🔓 Decrypted Message: HELLO

## 🧑‍💻 Author

Made with ❤️ by Lahari Naidu Kolli
