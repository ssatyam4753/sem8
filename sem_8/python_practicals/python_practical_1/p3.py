# Write a program to check whether given number is Armstrong number or not.


# main function
def main():
    number = int(input("enter number: "))
    # store number for future reference
    temp = number
    digits = len(str(number))
    print("number: ",number)
    print("number of digits in ",number," is: ",digits)
    # make a list of digits in the provided number
    lst = list(map(int,list(str(number))))
    '''for i in range(digits):
        lst.append(number%10)
        number = int(number/10)
    #print(lst)'''
    add = 0
    # calculate the addition of each digit powered to the number of digits in the number
    for element in lst :
        add = add + element ** digits
    print("sum of powers of each digit : ", add)
    # check if the number is armstrong
    if add == temp :
        print("the number is Armstrong number")
    else :
        print("the number is not armstrong")

if __name__ == "__main__" :
    main()
