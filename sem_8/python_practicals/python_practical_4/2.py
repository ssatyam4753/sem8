'''2) Write python programs for following sorting methods
    a) Selection sort
    b) Bubble sort
    c) Merge sort
    d) Insertion sort
    e) Quick sort
    f) Heap sort'''
import math

#method for Selection sort returns sorted list
def selSort(lst):
    l = len(lst)
    for i in range(l):
        min = lst[i]
        minIndex = i
        for j in range(i+1, l):
            if lst[j] < min :
                min = lst[j]
                minIndex = j
        # swap the first number in lst with min which is at minIndex
        lst[i], lst[minIndex] = lst[minIndex], lst[i]
    return lst

#method for Bubble sort returns sorted list
def bubSort(lst):
    l = len(lst)
    for i in range(l):
        for j in range(l-(i+1)):
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
        #print(lst)
    return lst


#merge method for merge sort
def merge(lst, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #create two temperorary lists
    L = list()
    R = list()

    # copy data into temperorary lists
    for i in range(n1):
        L.append(lst[l + i])
    for j in range(n2):
        R.append(lst[m + 1 + j])

    #merge temperorary lists into main list
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            lst[k] = L[i]
            i = i + 1
        else :
            lst[k] = R[j]
            j = j + 1
        k = k + 1

    # if any elements left in L[] copy to lst
    while i < n1 :
        lst[k] = L[i]
        i = i + 1
        k = k + 1

    # if any elements left in R[] copy to lst
    while j < n2 :
        lst[k] = R[j]
        j = j + 1
        k = k + 1


# method for merge sort; returns sorted list
def mergeSort(lst,l,r):
    if l < r :
        m = math.floor(( l + r ) / 2)
        mergeSort(lst,l,m)
        mergeSort(lst,m+1,r)
        merge(lst,l,m,r)
    return lst

# method for insertion sort returns sorted list
def insSort(lst):
    l = len(lst)
    for i in range(l):
        num = lst[i]
        j = i - 1
        while j >= 0 and num < lst[j] :
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = num
    return lst


# partition method for quickSort
def partition(lst,l,r):
    pivot = lst[r]
    i = l - 1
    for j in range(l,r):
        if lst[j] < pivot :
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[r] = lst[r], lst[i+1]
    return i+1


# method for quick sort; returns sorted list
def quickSort(lst,l,r):
    if l < r :
        pivot = partition(lst,l,r)
        quickSort(lst,l,pivot-1)
        quickSort(lst,pivot+1,r)
    return lst


def heapify(lst, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and lst[i] < lst[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and lst[largest] < lst[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]  # swap

        # Heapify the root.
        heapify(lst, n, largest)


# method for heap sort returns sorted list
def heapSort(lst):
    l = len(lst)

    # Build a maxheap.
    for i in range(l, -1, -1):
        heapify(lst, l, i)

    # One by one extract elements
    for i in range(l-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]   # swap
        heapify(lst, i, 0)
    return lst


def main():
    flag = True
    try :
        while flag is True:
            print("which sorting method you want to use: ")
            option = int(input("1 - selection sort\n2 - bubble sort\n3 - merge sort\n4 - Insertion sort\n5 - Quick sort\n6 - Heap sort\n7 - quit"))
            if option == 7:
                print("quitting....")
                return 0
            lst = list(map(int,input("enter numbers seperated by blankspace: ").split()))
            if len(lst) == 0:
                print("Empty list contains no elements, already sorted")
                return 0
            elif len(lst) == 1:
                print("list with 1 element needs no sorting")
                return 0

            print("list before sorting:",lst)
            if option == 1:
                #call selection sort with lst
                lst = selSort(lst)
                print("list sorted with selection sort:",lst)
            elif option == 2:
                #call bubble sort with lst
                lst = bubSort(lst)
                print("list sorted with bubble sort:",lst)
            elif option == 3 :
                #call merge sort with lst l(index of first element) and r(index of last element)
                r=len(lst)-1
                l = 0
                lst = mergeSort(lst,l,r)
                print("list sorted with merge sort:",lst)
            elif option == 4 :
                #call Insertion sort
                lst = insSort(lst)
                print("list sorted with merge sort:",lst)
            elif option == 5 :
                # call quick sort with list l(index of first element) and r(index of last element)
                l = 0
                r = len(lst)-1
                lst = quickSort(lst,l,r)
                print("list sorted with quick sort:",lst)
            elif option == 6:
                # call heap sort with list
                lst = heapSort(lst)
                print("list sorted with heap sort:",lst)
            else :
                print("invalid option selected")
    except :
        print("Something went wrong")
        return 1

if __name__ == "__main__":
    main()
