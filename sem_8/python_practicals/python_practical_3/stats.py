'''A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers. Define these functions
in a module named stats.py. Also include a function named mean, which computes
the average of a set of numbers. Each function should expect a list of numbers as
an argument and return a single number. Each function should return 0 if the list
is empty. Include a main function that tests the three statistical functions with a
given list.'''


def mean(lst) :
    if len(lst) == 0 :
        return 0
    temp = lst
    total = 0
    for i in lst :
        total = total + i
    avg = total / len(lst)
    return avg

def median(lst):
    if len(lst) == 0 :
        return 0
    lst.sort()
    print("list after sorting: ",end="")
    print(lst)
    med = 0
    temp = 0
    l = len(lst)
    if l % 2 != 0 :
        temp = (l//2 + 1)
        return lst[temp]
    else :
        temp = l//2
        return (lst[temp] + lst[temp + 1])/2

def mode(lst) :
    if len(lst) == 0 :
        return 0
    dct = dict()
    for i in lst :
        dct[i] = dct.get(i, 0) + 1
    #print(dct)
    max = 0
    key = 0
    for k,value in dct.items() :
        if value >= max :
            max = value
            key = k
    return key



def main():
    lst = list(map(int,input("enter numbers seperated by blankspace: ").split()))
    print("list of numbers:",lst)
    print("mode",mode(lst))
    print("mean",mean(lst))
    print("median",median(lst))


if __name__ == "__main__" :
    main()
