##### code for vigenere cipher (polyalphabetic cipher ) ####

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def find_pos(letter):
    for l in alphabet:
        if l == letter:
            return alphabet.index(l) + 1


# method to encrypt
def encrypt():
    temp = 0
    message = input("enter plaintext ")
    cipher = list()
    mlen = len(message)
    m = 0
    key = input("enter key ")
    while m < mlen:
        for k in key:
            if m < mlen:
                if (message[m].isalpha()):
                    temp = ord(message[m]) + find_pos(k.upper())
                    if temp >= 97 and temp <= 122:
                        cipher.append(chr(temp))
                    else:
                        cipher.append(chr(temp - 26))
                    m = m + 1
    print("ciphertext : \t", ''.join(cipher))


def decrypt():
    temp = 0
    ctext = input("enter ciphertext")
    key = input("enter key")
    clen = len(ctext)
    c = 0
    plain = list()
    while c < clen:
        for k in key:
            if c < clen:
                temp = ord(ctext[c]) - find_pos(k.upper())
                if temp >= 97 and temp <= 122:
                    plain.append(chr(temp))
                else:
                    plain.append(chr(temp + 26))
                c = c + 1
    print("plaintext : \t", ''.join(plain))


while True:
    try:
        print("###### MENU ####")
        print("1 encrypt\n2 decrypt\n0 exit ")
        choice = int(input())
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 0:
            break
        else:
            print("invalid choice\ttry again")
    except:
        print("#### invalid option ####")
