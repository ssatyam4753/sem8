# Write a program to print series of prime number in a range from 1 to input number.


'''trick :
            there is no need to check divisibility upto n-1, just check if the number is
            divisible by any prime number smaller than or equal to it's square root'''

#global variable
primes = list()

# main function
def main():
    #user input
    number = int(input("enter number: "))
    if number < 2 :
        print ("there are no prime numbers less than 2")
        return 0
    primes.append(2)
    for i in range(3, number+1) :
        if check_prime(i) == True :
            primes.append(i)
        else :
            continue
    print("prime numbers upto ",number)
    for prime in primes :
        print(prime,end="  ")
    print()

# function to check if a number is prime
def check_prime(i):
    sqrt = int(i**(0.5))
    for prime in primes :
        if prime <= sqrt :
            if i % prime == 0 :
                return False
            else :
                continue
        else :
            return True

if __name__ == "__main__":
    main()
