class Zero_sum:
    def finder(L):
        lst = []
        for i in range(len(L)):
            for j in range(len(L)):
                for k in range(len(L)):
                    for l in range(len(L)):
                        for m in range(len(L)):
                            s = L[i] + L[j] + L[k] + L[l] + L[m]
                            if s == 0:
                                temp = [L[i], L[j], L[k], L[l], L[m]]
                                if temp not in lst :
                                    lst.append(temp)
        return lst


def main():
    L = list(map(int,input("enter numbers: ").split()))
    print(Zero_sum.finder(L))

if __name__ == '__main__':
    main()