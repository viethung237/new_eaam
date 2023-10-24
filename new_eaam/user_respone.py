from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


with open('ciphertext_s_u.txt','rb') as response:
    data = response.read()

with open('private_key_user.pem','rb') as private_key_u:
    private_key_user = private_key_u.read()
    private_key_user_d = RSA.import_key(private_key_user)

decipher = PKCS1_OAEP.new(private_key_user_d)
decrypted_data = decipher.decrypt(data)
check_len = int(decrypted_data[len(decrypted_data) - 1 :].decode('utf-8'))
user_id_n = decrypted_data[:len(decrypted_data)-check_len-1]
sever_id = decrypted_data[len(decrypted_data)-check_len-1:len(decrypted_data)-1]
