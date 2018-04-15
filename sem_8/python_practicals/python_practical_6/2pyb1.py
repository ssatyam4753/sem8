from Crypto.Hash import MD5

string = input("enter string")
h = MD5.new()
h.update(string.encode())
print (h.hexdigest())