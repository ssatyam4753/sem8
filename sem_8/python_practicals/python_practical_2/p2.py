''' Define a function that can receive two integral numbers in string form and
    compute their sum and then print it in console.'''
def fun(str1,str2):
    int1 = int(str1)
    int2 = int(str2)
    ans = int1 + int2
    print(ans)

def main():
    str1 = input("enter number in string form: ")
    str2 = input("enter number in string form: ")
    fun(str1,str2)

if __name__ == "__main__" :
    main()
