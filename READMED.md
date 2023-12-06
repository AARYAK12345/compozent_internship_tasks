Malware Test Code
This repository contains a Python script designed to simulate a simple ransomware scenario for educational purposes. Note: Do not execute this code on any system or environment where data integrity is important.

What Does This Code Do?
The Python script within this repository demonstrates a basic ransomware concept by performing the following actions:

Key Generation: Generates RSA public and private keys, saving them into 'publickey.pem' and 'privatekey.pem' respectively.

AES Encryption: Asks for user input to specify an AES key, encrypts this key using the RSA public key, and saves it into 'aeskeyencrypted'.

File Encryption: Locates .txt files in the same directory as the script and encrypts them using AES encryption. The encrypted files are prefixed with 'encrypted_'.

Ransomware Simulation: After encrypting the files, it prompts the user with a question, simulating a ransom demand. If the user responds with "yes", it attempts to decrypt the files using the stored AES key.

Data Handling: It performs decryption and file handling based on the user's response.

Important Note: This code is for educational purposes only and demonstrates the concepts of encryption, ransomware, and decryption. Do not use this code for any malicious intent. Running this code can cause irreversible data loss.

Usage
Python Environment: Ensure you have Python installed to run this script.

Execution: Run the script in the desired environment using Python.

Interaction: Follow the prompts and exercise caution while interacting with the script.

Disclaimer: Using this code in any environment with valuable data or without proper authorization is strictly prohibited and may be illegal.
