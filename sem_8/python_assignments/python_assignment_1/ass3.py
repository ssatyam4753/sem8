#to retrieve url 
import urllib.request as ur

page = ur.urlopen("http://www.python.org")

print(page.read().decode())
#mybytes = page.read()

#mystr = mybytes.decode("utf8")
page.close()

#print(mystr)
