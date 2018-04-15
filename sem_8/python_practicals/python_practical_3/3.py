'''Write a program to convert each decimal number given in list to a fixed size binary
and generate a dictionary containing binary value as key and decimal number as
value.'''
def decToBin(lst):
    temp = list()
    keyList = list()
    for i in lst:
        print(i)
        while i//2 != 0:
            temp.append(i%2)
            i = i //2
        if i == 0 :
            temp .append(0)
        else :
            temp.append(1)
        while len(temp) < 8 :
            temp.append(0)
        temp.reverse()
        key = ''.join(map(str,temp))
        keyList.append(key)
        temp[:] = []
    dct = dict()
    for i in range(len(lst)):
        dct[keyList[i]] = lst[i]
    return dct


def main():
    lst = list(map(int,input("enter decimal numbers seperated by a blankspace: ").split()))
    print(lst)
    print(decToBin(lst))

if __name__ == "__main__":
    main()
