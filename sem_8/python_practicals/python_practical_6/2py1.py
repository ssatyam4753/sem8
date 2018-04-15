from Crypto.Cipher import AES

def main():
    key = input("enter 16 digit key")
    if len(key) != 16:
        print("invalid key")
        return 1
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    message = input("enter message")

    while len(message)%16 != 0:
        message += '!'
    print("text after padding: ",message)
    ciphertext = obj.encrypt(message)
    print("encrypted text: ",ciphertext)
    obj2 = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    plaintext = obj2.decrypt(ciphertext)
    print("plaintext: ",plaintext)


if __name__ == '__main__':
    main()