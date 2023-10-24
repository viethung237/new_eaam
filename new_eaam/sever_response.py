sever_id = b'654321'

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP

# khoa rsa cho sever
key = RSA.generate(1024)  #1024 bit

private_key = key.export_key()
with open("private_key_sever.pem", "wb") as private_key_file:
    private_key_file.write(private_key)

public_key = key.publickey().export_key()
with open("public_key_sever.pem", "wb") as public_key_file:
    public_key_file.write(public_key)

#########################
####nhan request
with open('initial.txt','rb') as request:
    user_id_n = request.read()

####Hash
hash_obj = SHA256.new()

hash_obj.update(user_id_n)

hash_user_id_n = hash_obj.digest()
#####Encrypt
with open('public_key_user.pem','rb') as public_key_u:
    public_key_user = public_key_u.read()
    public_key_user_e = RSA.import_key(public_key_user)

cipher = PKCS1_OAEP.new(public_key_user_e)
encrypted_sever = cipher.encrypt(hash_user_id_n+sever_id+b'6')

####send
with open('ciphertext_s_u.txt','wb') as response:
    response.write(encrypted_sever)

