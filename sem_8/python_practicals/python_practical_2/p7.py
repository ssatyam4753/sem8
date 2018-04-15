'''     Please write a program to randomly generate a list with 5 numbers, which are
        divisible by 5 and 7 , between 1 and 1000 inclusive.'''

import random

def main():
    count = 0
    lst = list()
    while count < 5:
        i = random.randint(1,1000)
        #print(i)
        if i % 7 == 0 and i % 5 == 0 :
            if i not in lst:
                lst.append(i)
                count = count + 1
            else :
                continue
    print(lst)



if __name__ == "__main__" :
    main()
