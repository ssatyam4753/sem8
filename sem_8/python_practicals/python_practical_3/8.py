'''8.Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]'''

def removeDuplicates(lst):
    ltemp = list()
    for item in lst:
        if item not in ltemp:
            ltemp.append(item)
    return ltemp

def main():
    lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    lst = removeDuplicates(lst)
    print(lst)

if __name__ == "__main__" :
    main()
