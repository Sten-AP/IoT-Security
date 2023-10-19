import math


def decrypt_transpositie(encrypted_bericht, sleutel):
    numOfColumns = math.ceil(len(encrypted_bericht) / sleutel)
    numOfRows = sleutel

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(encrypted_bericht)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for symbol in encrypted_bericht:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext).replace("_", "")
