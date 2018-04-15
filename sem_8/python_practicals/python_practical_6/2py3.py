
from Crypto.Cipher import DES3
from Crypto import Random
#key = 'Sixteen byte key'
key = input("enter key of size 16 or 24")
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = input("enter message")
while len(plaintext)%8 != 0:
    plaintext += 'x'
encrypted_text = cipher_encrypt.encrypt(plaintext)
print(encrypted_text)
cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) #you can't reuse an object for encrypting or decrypting other data with the same key.
plaintext = cipher_decrypt.decrypt(encrypted_text)
print(plaintext)
