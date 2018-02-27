# Write a program to check if the input year is leap year or not.

''' logic :
            A year is leap year if following conditions are satisfied
            1) Year is multiple of 400
            2) Year is multiple of 4 and not multiple of 100.
            '''

def leapcheck(year):
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0:
                return True
            else :
                return False
        else :
            return True
    else :
        return False


def main():
    year = int(input("enter year: "))
    res = leapcheck(year)
    if res == True :
        print(year, " is a leap year")
    else :
        print(year, " is not a leap year")

if __name__ == "__main__":
    main()
