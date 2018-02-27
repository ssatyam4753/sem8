''' To know the current working directory and print all content of current directory. what changes do we need to make in program, if
we wish to display, the content of only "mysub" directory available in current directory '''

import os

cur_dir = os.getcwd()
print(cur_dir)
print("contents of current working directory:")
print(os.listdir(path='.'))  #or print(os.listdir(path=cur_dir))
print("contents of mysub directory")
print(os.listdir(path='./mysub'))
#or
#mysub = cur_dir + '/mysub'
#print(os.listdir(path=mysub))
