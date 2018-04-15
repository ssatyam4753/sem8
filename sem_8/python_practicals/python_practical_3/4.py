'''Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers in
several bases.'''

def decimalToRep(n,base):
    conversionString = "0123456789ABCDEF"
    if n < base:
        return conversionString[n]
    else:
        return decimalToRep(n//base,base) + conversionString[n%base]

def main():
    num = int(input("enter integer:"))
    base = int(input("enter base"))
    print(decimalToRep(num,base))

if __name__ == "__main__":
    main()
