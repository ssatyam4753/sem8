def filesfun():
    file_name = input("enter file name: ")
    print(file_name)
    fh = open(file_name, 'r+')
    lines = fh.readlines()
    for i in range(1 , len(lines)+1):
        print(i,end=" ")
        print(lines[i-1],end="")
    num = int(input("enter a valid line number(0 to quit)"))
    if num == 0 :
        return 0
    print(lines[num-1])


def main():
    filesfun()

if __name__ == "__main__":
    main()
