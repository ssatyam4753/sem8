def uniquewords():
    fh = open('sec.txt','r+')
    data = fh.read()
    lst = data.strip().split()
    lst = list(set(lst))
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
    lst.sort()
    for i in lst:
        print(i)

uniquewords()
