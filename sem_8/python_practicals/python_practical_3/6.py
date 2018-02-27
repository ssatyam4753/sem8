def concordance():
    fh = open('sec.txt','r')
    data = fh.read()
    lst = data.strip().split()
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
    lst.sort()
    dct = dict()
    for i in lst:
        dct[i] = dct.get(i,0)+1
    for key, value in sorted(dct.items()):
        print("%-15s %-5d"% (key,value))

concordance()
