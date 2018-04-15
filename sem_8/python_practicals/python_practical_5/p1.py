'''Write a Python program to create a class that perform basic Calculator
operation.'''


class calc:
    __a = None
    __b = None

    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def add(self):
        return self.__a + self.__b

    def sub(self):
        return self.__a - self.__b

    def mul(self):
        return self.__a * self.__b

    def div(self):
        if self.__b == 0:
            print("division by zero not allowed")
        else:
            return self.__a / self.__b

    def mod(self):
        if self.__b == 0:
            print("modulo by zero not allowed")
        else:
            return self.__a % self.__b


def main():
    a = int(input("enter a"))
    b = int(input("enter b"))
    A = calc(a, b)
    print("sum of a and b:", A.add())
    print("difference of a and b:", A.sub())
    print("product of a and b:", A.mul())
    print("division of a and b:", A.div())
    print("remainder of a and b:", A.mod())


if __name__ == '__main__':
    main()
