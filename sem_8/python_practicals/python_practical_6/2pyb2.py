from Crypto.Hash import SHA256

string = input("enter string")
print(SHA256.new(string.encode()).hexdigest())