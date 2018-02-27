

def main() :
    fp = open("info.txt","r+")
    for line in fp :
        lst = line.strip().split(" ")
        #print(lst)
        for word in lst :
            word = word.strip(',.')
            if len(word) == 5 :
                if 'm' in word :
                    print(word)
                else :
                    continue



if __name__ == "__main__" :
    main()
