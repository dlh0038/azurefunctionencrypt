from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

priv_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

pub_key = priv_key.public_key()

priv_pem = priv_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())

pub_pem = pub_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

with open('private.pem', 'wb') as f:
    f.write(priv_pem)

with open('public.pem', 'wb') as f:
    f.write(pub_pem)