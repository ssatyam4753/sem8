def encryption_key(key):
    order = []
    temp = []
    for k in range(len(key)):
        order.append((key[k],k))
    order.sort()
    print(order)
    for i in order:
        temp.append(i[1])
    return temp


def encrypt(plaintext, key):
    cipher = []
    block_size = len(key)
    while len(plaintext) % block_size != 0:
        plaintext += 'x'
    i = 0
    temp = list()
    for j in range(0,len(plaintext)//block_size):
        temp.append(plaintext[i:i+block_size])
        i += block_size
    print(temp)
    order = encryption_key(key)
    for i in order:
        for j in range(len(plaintext) // block_size):
            cipher.append(temp[j][i])
    print(''.join(cipher))


def decryption_key(key):
    temp = encryption_key(key)
    print(temp)
    order = []
    for i in range(len(temp)):
        order.append((temp[i], i))
    order.sort()
    print(order)
    temp[:] = []
    for i in order:
        temp.append(i[1])
    return temp



def decrypt(ciphertext, key):
    block_size = len(key)
    print(block_size)
    plain= []
    temp = []
    i = 0
    for j in range(block_size) :
        temp.append(ciphertext[i:i+(len(ciphertext)//block_size)])
        i += len(ciphertext)//block_size
    print(temp)
    order = decryption_key(key)
    for i in order:
        plain.append(temp[i])
    print(plain)
    temp[:] = []
    for i in range(block_size-1):
        for j in range(len(plain)):
            temp.append(plain[j][i])
    print(''.join(temp))



def main():
    text = input("enter text")
    text = text.strip().replace(" ", "").lower()
    key = input("enter key")
    key = key.lower()
    ch = int(input("1.Encryption\n2.Decryption"))
    if ch == 1:
        encrypt(text, key)
    elif ch == 2:
        decrypt(text, key)
    else:
        print('Invalid command.')

if __name__ == '__main__':
    main()