'''Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
"#800000", "#FFFF00"]'''

def listToDict():
    lists = list()
    colorName = input("enter names of color seperated by space: ").split()
    colorCode = input("enter codes of the colors int the same order separated by blankspace").split()
    dct = list()
    for color, code in zip(colorName,colorCode):
        dct.append({'colorName':color,'colorCode':code})
    return dct

def main():
    lst = listToDict()
    print(lst)

if __name__ == "__main__" :
    main()
