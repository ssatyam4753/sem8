def encrypt(clearText, key):
    # empty cipher
    result = ""
    matrix = [["" for x in range(len(clearText))] for y in range(key)]
    increment = 1
    row = 0
    col = 0
    for c in clearText:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1
        matrix[row][col] = c
        row += increment
        col += 1
    for list in matrix:
        result += "".join(list)
    return result


def decrypt(cipherText, key):
    # empty plainText
    result = ""
    matrix = [["" for x in range(len(cipherText))] for y in range(key)]
    idx = 0
    increment = 1
    for selectedRow in range(0, len(matrix)):
        row = 0
        for col in range(0, len(matrix[row])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            if row == selectedRow:
                matrix[row][col] += cipherText[idx]
                idx += 1
            row += increment
    matrix = transpose(matrix)
    for list in matrix:
        result += "".join(list)
    return result


def transpose(m):
    result = [[0 for y in range(len(m))] for x in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result


def main():
    ch = str(input('choose e. Encryption\nd. Decryption...: '))
    # plain text
    text = str(input('Enter Message...: '))
    text = text.replace(' ', '').strip()
    print(text)
    # key in terms of levels
    key = int(input('Enter Key...: '))
    if ch == 'e':
        # Encryption
        cipherText = encrypt(text, key)
        print("Ciphered Text: %s" % cipherText)
    elif ch == 'd':
        # Decryption
        decipherText = decrypt(text, key)
        print("Deciphered Text: %s" % decipherText)
    else:
        print('Enter valid operation')


if __name__ == '__main__':
    main()
