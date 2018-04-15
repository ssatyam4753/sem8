from Crypto.Cipher import DES

from Crypto import Random

iv = Random.get_random_bytes(8)
key = input("enter 8 bit key")
if len(key) != 8:
    print("invalid key")
des1 = DES.new(key, DES.MODE_CFB, iv)

des2 = DES.new(key, DES.MODE_CFB, iv)

text = input("enter text")

cipher_text = des1.encrypt(text)
print("cipher_text:", cipher_text)
plaintext = des2.decrypt(cipher_text)
print(plaintext)
