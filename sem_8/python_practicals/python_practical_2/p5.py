'''     Define a function which can generate a dictionary where the keys are numbers
        between 1 and 20 (both included) and the values are square of keys. The
        function should just print the values only.'''

def fun():
    dct = dict()
    for key in range(1 , 20+1):
        dct[key] = key ** 2
    print(dct.values())

def main():
    fun()

if __name__ == "__main__" :
    main()
