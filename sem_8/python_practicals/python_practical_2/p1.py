# Define a function that can convert a integer into a string and print it in console.

def main() :
    inp = int(input("enter integer: "))
    int_to_str(inp)

def int_to_str(inp):
    a = str(inp)
    print(a)

if __name__ == "__main__" :
    main()
