'''     Define a function which can print a dictionary where the keys are numbers
        between 1 and 3 (both included) and the values are square of keys.'''

def fun():
    dct = dict()
    for i in range(1,3+1):
        dct[i] = i ** 2
    print(dct)

def main():
    fun()

if __name__ == "__main__" :
    main()
