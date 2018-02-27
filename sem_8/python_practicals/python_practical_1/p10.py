'''Write a Python program to print the following string in a specific format.
String: Twinkle, twinkle, little star, How I wonder what you are! Up above the world
so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what
you are
Output :
    Twinkle, twinkle, little star,
        How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
    Twinkle, twinkle, little star,
        How I wonder what you are'''

def main():
    # method 1: use escape characters
    text = "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tup above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are"
    print(text)

    # method 2: use ''' special multiline single string
    text = '''
Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are'''
    print(text)

if __name__ == "__main__" :
    main()
