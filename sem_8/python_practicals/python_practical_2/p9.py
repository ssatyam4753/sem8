'''     You are given a string.
        Your task is to print all possible permutations of size of the string in lexicographic sorted order.
        Input Format
        A single line containing the space separated string and the integer value.
        Constraints
        The string contains only UPPERCASE characters.
        Output Format
        Print the permutations of the string on separate lines.'''

from itertools import permutations

def main():
    temp,num = input("enter string and the integer value seperated by space :").split()
    num = int(num)
    chList = list()
    for i in temp:
        chList.append(i)
    perm = list(permutations(chList,num))
    for i in range(len(perm)):
        perm[i] = ''.join(perm[i])
    perm.sort()
    for item in perm:
        print(item)


if __name__ == "__main__":
    main()
