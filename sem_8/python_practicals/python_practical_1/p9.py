'''     problem statement:-
        Write a Python program to create all possible unique strings by using 'a', 'e', 'i', 'o',
        'u'. Use the characters exactly once.'''

def words(letters,word=''):
    if len(word) == 5 :
        print(word)
    for letter in letters :
        words(letters - {letter}, word + letter)



def main():
    words(set("aeiou"))


if __name__ == "__main__":
    main()
