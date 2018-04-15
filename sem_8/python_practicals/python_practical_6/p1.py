
def cipher(mode):
    S = input("enter message: ")
    key = int(input("enter key"))
    S = S.lower()
    print(S)
    if mode == '1':
        pass
    elif mode == '2':
        key = -1 * key
    print(key)
    lst = list()
    l = len(S)
    for i in range(l):
        if S[i].isalnum():
            if S[i].isalpha():
                if ord(S[i])+key > ord('z') or ord(S[i])+key < ord('a'):
                    print(chr((((ord(S[i])-ord('a'))+key)%26)+ord('a')), end="")
                else:
                    print(chr(ord(S[i])+key), end="")
            elif S[i].isnumeric():
                if ord(S[i])+key > ord('9'):
                    print(chr((((ord(S[i])-ord('0'))+key)%10)+ord('0')),end="")
                else:
                    print(chr(ord(S[i])+key),end="")
        else :
            print(S[i],end="")

def main():
    mode = input("1.Encrypt\n2.Decrypt")
    cipher(mode)

if __name__ == "__main__":
    main()