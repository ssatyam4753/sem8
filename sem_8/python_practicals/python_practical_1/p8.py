''' problem statement:-
        Write a Python program which accepts the user's first and last name and print them
        in reverse order with a space between them.'''


#main function
def main():
    while True :
        first = input("enter first name: ")
        last = input("enter last name: ")
        name = last+" "+first
        print(name)
        print("enter 0 to exit anything else to continue: ")
        flag = input()
        if flag == '0' :
            return 0
        else:
            continue

if __name__ == "__main__" :
    main()
