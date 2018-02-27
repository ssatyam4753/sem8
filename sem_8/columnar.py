import math
MAX = 256

# function to encrypt using given key
def encrypt(plainText,key):
    plainTextRows = rowColConversion(plainText,key)
    keylst = list()

    # make a list containing ascii values of key characters without changing the order
    for i in key:
        keylst.append(ord(i))
    #print(keylst)
    cipherText = list()

    # deal with the keys that have repeating letters
    for i in range(len(keylst)):
        for j in range(len(keylst)) :
            if keylst[i] == keylst[j] and i < j :
                keylst[j] = keylst[j] + 1

    # list to store the order in which columns must be read
    order = list()

    # generate order
    for i in range(len(keylst)):
        min = MAX
        minIndex = 0
        for j in range(len(keylst)):
            if keylst[j] < min :
                min = keylst[j]
                minIndex = j
        #print(keylst)
        keylst[minIndex] = MAX
        order.append(minIndex)
    print(order)

    # generate cipherText
    for j in order :
        for i in range(math.ceil(len(plainText)/len(key))) :
            cipherText.append(plainTextRows[i][j])

    cipherTextString = ''.join(cipherText)
    print(cipherTextString)


# method for decryption
def decrypt(cipherText,key):
    cipherTextRows = colRowConversion(cipherText,key)
    keylst = list()

    # make a list containing ascii values of key characters without changing the order
    for i in key:
        keylst.append(ord(i))
    #print(keylst)
    plainText = list()

    # deal with the keys that have repeating letters
    for i in range(len(keylst)):
        for j in range(len(keylst)) :
            if keylst[i] == keylst[j] and i < j :
                keylst[j] = keylst[j] + 1

    # list to store the order for exchanging the columnes back
    order = list()

    # generate order
    for i in range(len(keylst)):
        min = MAX
        minIndex = 0
        for j in range(len(keylst)):
            if keylst[j] < min :
                min = keylst[j]
                minIndex = j
        #print(keylst)
        keylst[minIndex] = MAX
        order.append(minIndex)

    #order = list(reversed(order))
    print(order)

    # generate order in which it must be read to decipher
    decOrder = list()
    for i in range(len(order)):
        min = MAX
        minIndex = 0
        for j in range(len(order)):
            if order[j] < min :
                min = order[j]
                minIndex = j
        order[minIndex] = MAX
        decOrder.append(minIndex)
    print(decOrder)

    # generate plainText
    itr = math.ceil(len(cipherText)/len(key))
    for i in range(itr) :
        for j in decOrder :
            plainText.append(cipherTextRows[i][j])
    print(''.join(plainText))


# rowColConversion returns a list of lists each sublist of size of key
def rowColConversion(Text,key):
    # length of individual rows equal to the length of the key
    rowLength = len(key)
    tLength = len(Text)
    chlst = list()

    # chlst is the list of all individual elements in the plainText
    for ch in Text:
        chlst.append(ch.lower())
    index = 0
    TextRows = list()
    temp = list()

    #itr to calculate total numbers of rows to transform into rows
    itr = math.ceil(tLength / rowLength)
    #print("itr:",itr)

    # create a list of lists to use as rows and columns
    for i in range(itr):
        for j in range(rowLength):
            temp.append(chlst[index])
            index = index + 1
            if index >= tLength :
                break
        #print(temp)
        TextRows.append(temp[:])
        temp[:] = []

    # append blankspaces in the last row if there are not less elements than rowSize
    for i in TextRows:
        if len(i) < rowLength :
            while len(i) < rowLength :
                i.append(" ")
        print(i)

    return TextRows

def colRowConversion(Text,key):
    # length of individual rows equal to the length of the key
    rowLength = len(key)
    tLength = len(Text)
    chlst = list()

    # chlst is the list of all individual elements in the cipherText
    for ch in Text:
        chlst.append(ch.lower())
    index = 0
    TextRows = list()
    temp = list()

    #itr to calculate total numbers of rows to transform into rows
    itr = math.ceil(tLength / rowLength)

    #append blankspaces at the end of cipherText if missing in cipherText
    while len(chlst) < itr * rowLength :
        chlst.append(" ")

    # create a list of lists to use as rows and columns
    for i in range(rowLength):
        for j in range(itr):
            temp.append(chlst[index])
            index = index + 1
        TextRows.append(temp[:])
        temp[:] = []
    print(TextRows)

    #transpose matrix
    TextRows = [list(x) for x in zip(*TextRows)]

    for item in TextRows :
        print(item)
    return TextRows


def main():
    choice = input("enter e to encrypt d to decrypt: ")
    if choice == 'e':
        plainText = input("enter plaintext: ")
        key = input("enter key(string): ")
        encrypt(plainText,key)
    elif choice == 'd' :
        cipherText = input("enter cipherText: ")
        key = input("enter key: ")
        decrypt(cipherText,key)
    else :
        print("invalid input:",choice,)

if __name__ == "__main__" :
    main()
