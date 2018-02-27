'''     Write a program which will find all such numbers which are divisible by 7 but are not
        a multiple of 5, between 5000 and 5999 (both included). The numbers obtained
        should be printed in a comma-separated sequence on a single line.'''

#main function
def main():
    lst = list()
    for i in range(5000 , 5999+1):
        if i % 7 == 0 :
            if i % 5 == 0 :
                continue
            else :
                lst.append(i)
    for element in lst:
        print(element,end=",")

# invoke main
if __name__ == "__main__" :
    main()
