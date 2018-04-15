class Counter:
    def count(sentence):
        digits = 0
        letters = 0
        for i in sentence:
            if i.isdigit():
                digits += 1
            if i.isalpha():
                letters += 1
            else:
                continue
        print("LETTERS: ", letters)
        print("DIGITS: ", digits)


def main():
    sentence = input("enter sentence")
    Counter.count(sentence)


if __name__ == '__main__':
    main()
