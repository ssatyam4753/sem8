'''3) Write a python program to create hash table using following hash
methods with chaining as a collision resolution method:
c) Binning Method'''

def binningHash(n):
    l = len(str(n))
    keyGenerator = 10 ** (l-1)
    hashKey = n // keyGenerator
    return hashKey

def search(num,hashTable):
    hashKey = binningHash(num)
    for i in hashTable[hashKey]:
        if num == i :
            print(num, "found in bin with hashkey ",hashKey)
            return 0
    return 1

def main():
    flag = True
    hashTable = dict()
    print("length of hash table is 10")
    s = 10
    for i in range(s):
        hashTable[i] = []
    print(hashTable)

    while flag is True :
        try :
            n = input("enter number to add in hash table\ns to enter search mode: ")
        except :
            print("stopping program")
            return 2
        if n == 's':
            num = int(input("enter number to search: "))
            res = search(num,hashTable)
            if res == 1:
                print("item not found")
                return 0
            return 0
        n = int(n)
        hashKey = binningHash(n)
        hashTable[hashKey].append(n)
        print("current state of hash table:\n")
        for key, value in hashTable.items() :
            print(key,value)

if __name__ == "__main__":
    main()
