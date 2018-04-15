'''1) Write python programs for following searching methods
a) Linear search
b) Binary search'''

#lSearch performs a linear search on the given numList to find the number num and returns the index+1 and 0 if num not found
def lSearch(numList,num):
    for i in range(len(numList)):
        if numList[i] == num :
            return i+1
    return 0



#bSearch performs a Binary search on given numList to find num
def bSearch(numList,num):
    left = 0
    right = len(numList)-1
    numList.sort()
    while(left <= right):
        mid = (left+right) // 2
        if numList[mid] == num :
            return mid+1
        elif num < numList[mid] :
            right = mid - 1
        else :
            left = mid + 1
    return 0




def main():
    lst = list(map(int,input("enter numbers seperated by blankspace: ").split()))
    if len(lst) == 0 :
        print("Empty list contains no elements, search would be worthless")
        return 0
    num = int(input("enter number to search: "))
    print("performing linear search for number:",num)
    index = lSearch(lst,num)
    if index == 0:
        print("number: ",num,"not in list")
    else :
        print("number: ",num,"found at index: ",index-1)

    print("performing binary search for number:",num)
    index = bSearch(lst,num)
    if index == 0:
        print("number: ",num,"not in list")
    else :
        print("number: ",num,"found at index: ",index-1)
    return 0

if __name__ == "__main__":
    main()
