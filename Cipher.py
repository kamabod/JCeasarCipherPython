#!usr/bin/pyhon

from array import*


def split_str(plainText):
    plainTextArray = [ch for ch in plainText]
    return plainTextArray

def encrypt(plainText, offset):
    alphabetSize = 26
    letterA = 65
    lettera = 97
    encodedText = ""
    plainTextArray = split_str(plainText)

    n = 1
    for i in range(0, len(plainTextArray), n):
        numericalVal = ord(plainTextArray[i])
        if (plainTextArray[i].isupper()):
            print(numericalVal)
            encodedText = encodedText + \
                chr((numericalVal+offset-letterA) % alphabetSize+letterA)
        elif(numericalVal == 32):
            encodedText = encodedText + plainTextArray[i]
        else:
            encodedText = encodedText + \
                chr(((numericalVal + offset - lettera) %
                     alphabetSize) + lettera)

    print(encodedText)

    return encodedText

def main():
    encrypt("ab", 2)

if __name__ == "__main__":
    main()