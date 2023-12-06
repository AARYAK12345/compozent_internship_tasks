import rsa
publickey,privatekey=rsa.newkeys(2048)
with open("publickey.pem","wb") as f:
    f.write(publickey.save_pkcs1("PEM"))
with open("privatekey.pem","wb") as f:
    f.write(privatekey.save_pkcs1("PEM"))

with open("publickey.pem",'rb') as f:
    publickey1=rsa.PublicKey.load_pkcs1(f.read())
with open("privatekey.pem",'rb') as f:
    privatekey1=rsa.PrivateKey.load_pkcs1(f.read())

aeskey=input("ENTER THE AES KEY YOU WANT: ")
encryptedmessage=rsa.encrypt(aeskey.encode(),publickey1)

with open("aeskeyencrypted","wb") as f:
    f.write(encryptedmessage)



