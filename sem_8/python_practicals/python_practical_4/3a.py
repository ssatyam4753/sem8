'''3) Write a python program to create hash table using following hash
methods with chaining as a collision resolution method:
a) Folding Method
'''
import math

# method to calculate hash
def foldingHash(n,s):
    #print(n)
    fold = list()
    l = len(str(n))
    temp = list()
    # reverse the input number
    for ch in str(n):
        temp.append(ch)
    temp = list(reversed(temp))
    n = int(''.join(temp))
    #print(n)
    # divive number into blocks of size 3 or less
    foldSize = math.ceil(l / 3)
    for i in range(foldSize):
        fold.append(n % 1000)
        n = n // 1000
    #print(fold)
    #reverse the numbers inside fold to make them as they were in original number
    for i in range(len(fold)):
        temp[:] = []
        for ch in str(fold[i]):
            temp.append(ch)
        temp = list(reversed(temp))
        fold[i] = int(''.join(temp))
    print("fold: ",fold)
    total = sum(i for i in fold)
    print("sum of all folds:",total)
    print("hash key:",total%s)
    return total % s


def search(num,hashTable,s):
    hashKey = foldingHash(num,s)
    for i in hashTable[hashKey]:
        if i == num:
            print(num,"found in the hashTable with hashkey",hashKey)
            return 0
    return 1


def main():
    flag = True
    hashTable = dict()
    s = int(input("enter size of hash table: "))
    for i in range(s):
        hashTable[i] = []
    print(hashTable)
    #print(hashTable)
    while flag is True :
        try :
            n = input("enter number to add in hash table s to enter search mode anything else to quit: ")
            if n == 's':
                num = int(input("enter number to search: "))
                res = search(num,hashTable,s)
                if res == 1 :
                    print("item not found in hash table")
                return 0
            else :
                n = int(n)
        except :
            print("stopping program")
            return 2
        hashKey = foldingHash(n,s)
        hashTable[hashKey].append(n)
        print("current state of hash table:\n")
        for key, value in hashTable.items() :
            print(key,value)




if __name__ == "__main__":
    main()
