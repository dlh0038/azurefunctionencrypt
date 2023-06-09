from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

#load private key
with open("/home/user/Documents/azurefunction/private.pem", 'rb') as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)

#load ciphertext
with open("/home/user/Documents/azurefunction/test_encrypt.txt", 'rb') as cipherfile:
    ciphertext = cipherfile.read()

plaintext = private_key.decrypt(ciphertext, 
                    padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                ))

print(plaintext)