# Write a program to print Fibonacci sequence till input number using while loop.

def main():
    N = int(input("enter number: "))
    if N < 0 :
        print("invalid input")
        return 0
    if N == 0 :
        return 0

    # initialise first fibonacci numbers
    first = 0
    second = 1
    while first <= N :
        print(first,end = " ")
        first, second = second, first+second

if __name__ == "__main__":
    main()
