
fp = open("student.txt",'r')
for line in fp :
    lst = line.split(" ")
    print("name: ",lst[0]," DOB: ",lst[1])
