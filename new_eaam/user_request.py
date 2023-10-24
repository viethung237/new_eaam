from function import *
import secrets
from Crypto.PublicKey import RSA
user_id = b'123456'

# Tạo một cặp khóa RSA
key = RSA.generate(1024)  #1024 bit

private_key = key.export_key()
with open("private_key.pem", "wb") as private_key_file:
    private_key_file.write(private_key)

public_key = key.publickey().export_key()
with open("public_key.pem", "wb") as public_key_file:
    public_key_file.write(public_key)


def random_n(length):
    random_id = ''.join(secrets.choice('0123456789') for _ in range(length))
    return random_id.encode('utf-8')

with open('phase.txt','wb') as memory:
    memory.write(user_id+random_n(6))


