import numpy as np

KEY = [[ 8,  6,  9, 5  ],
       [ 6,  9,  5, 10 ],
       [ 5,  8,  4, 9  ],
       [ 10, 6, 11, 4  ]]


def encrypt(plaintext,key):
    plaintext = plaintext.lower()
    cipher = ''
    block_size = len(key)
    while len(plaintext) % block_size != 0:
        plaintext += 'x'
    matrix = np.array(key)
    arr = [ord(i) - ord('a') for i in plaintext]
    count = 0
    for ch in plaintext:
        if str.isalpha(str(ch)):
            cipher += chr(sum(matrix[count % block_size] * arr) % 26 + ord('a'))
            count += 1
    print(cipher)



def decrypt(ciphertext,key):
    cipher = ''
    block_size = len(key)
    matrix = (np.linalg.inv(key) + 26) % 26
    ciphertext = ciphertext.lower()
    arr = np.array([ord(i) - ord('a') for i in ciphertext], dtype=int)
    count = 0
    for ch in ciphertext:
        if str.isalpha(str(ch)):
            number = sum(matrix[count % block_size] * arr) % 26
            cipher += chr(int(str(number)[:-2]) + ord('a'))
            count += 1
    print(cipher)


def main():
    text = input("enter text")
    ch = input("1.enter key matrix\n2.Use default key matrix")
    if ch == '1':
        key = input("enter key matrix")
    elif ch == '2' :
        key = KEY
    else:
        print("invalid option")
        return 1
    ch = input("1.encrypt\n2.Decrypt")
    if ch == '1':
        encrypt(text,key)
    elif ch == '2':
        decrypt(text,key)
    return 0


if __name__ == '__main__':
    main()