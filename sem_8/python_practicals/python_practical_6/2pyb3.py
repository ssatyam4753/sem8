from Crypto.Hash import SHA512

string = input("enter string")
print(SHA512.new(string.encode()).hexdigest())