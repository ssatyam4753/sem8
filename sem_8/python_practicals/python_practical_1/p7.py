''' Write a program which can compute the factorial of a given numbers. The results
    should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program: 8 Then, the output should
    be: 40320'''

#main function
def main() :
    # take input space seperated single or multiple values and store them in list
    numbers = list(map(int,input("enter numbers seperated by blankspace: ").split(" ")))

    # list to store factorials
    facts = list()
    for number in numbers :
        fact = compute_factorial(number)
        facts.append(fact)
    for fact in facts:
        print(fact,end=",")
    print()


# function to compute factorial
def compute_factorial(number) :
    if number == 0 :
        return 1
    if number > 0 :
        return number * compute_factorial(number-1)

if __name__ == "__main__" :
    main()
