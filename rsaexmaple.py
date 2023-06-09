from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

with open("/home/user/Documents/azurefunction/public.pem", 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())

print(f"public key {public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)}")