#to append data into an existing file, get data from user and append it then display the contents of file
import os
fp = open("myfile.txt",'a+')
print("contents of file before appending data")
fp.seek(0, os.SEEK_SET)
print(fp.read())
inp = input("enter data to be appended to the file")
fp.write(inp)
print("content of file after appending user's data")
# seek file pointer to the begining of the file
fp.seek(0, os.SEEK_SET)
print(fp.read())
fp.close()
