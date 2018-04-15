'''3) Write a python program to create hash table using following hash
methods with chaining as a collision resolution method:
b) Mid-square Method
'''

def midSquareHash(n):
    l = len(str(n))
    square = n ** 2
    temp = list()
    square = str(square)
    #zfill is used to padd zeros to string
    square = square.zfill(l*2)
    hashKey = square[l-1]+square[l]
    print("square:", square,"hashKey:",hashKey)
    return int(hashKey)

def search(num,hashTable):
    hashKey = midSquareHash(num)
    for i in hashTable[hashKey]:
        if i == num:
            print(num,"found in the hashTable with hashkey",hashKey)
            return 0
    return 1


def main():
    flag = True
    hashTable = dict()
    print("length of hash table is 100")
    s = 100
    for i in range(s):
        hashTable[i] = []
    #print(hashTable)
    while flag is True :
        try :
            n = input("enter number to add in hash table or s to enter search mode: ")
            if n == 's':
                num = int(input("enter number to search: "))
                res = search(num,hashTable)
                if res == 1 :
                    print("item not found in hash table")
                return 0
            else :
                n = int(n)
        except :
            print("stopping program")
            return 2
        hashKey = midSquareHash(n)
        hashTable[hashKey].append(n)
        #print("current state of hash table:\n")
        #for key, value in hashTable.items() :
        #    print(key,value)




if __name__ == "__main__" :
    main()
