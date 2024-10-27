# columnConverter.py
# Author: Ashok Khare
# Converts 1-based numeric spreadsheet column labels to their letter equivalents, in the style of Excel or Google Sheets.
# Example: 3 => C, 27 => AA

# Process
# Number-to-letter map (base 26):
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 0/26
# A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# matchingLetter(int) = chr(ord('A') + int - 1) if int != 0 || "Z" if int == 0
# If remainder[i] == 0, quotient[i] -= 1

def convertNumericColumnLabel(number):
    letters = []
    quotient = number

    while (quotient != 0):
        remainder = quotient % 26
        quotient = quotient // 26
        if (remainder == 0):
            quotient -= 1
            letters.append('Z')
        else:
            letters.append(chr(ord("A") + remainder - 1))

    letters.reverse()
    return "".join(letters)

if __name__ == "__main__":
    for i in range(1, 703):
        print(i, convertNumericColumnLabel(i))