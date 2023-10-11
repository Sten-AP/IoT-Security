import math

sleutel = "iot"
bericht = "HELLOWORLD"


# def encrypt_transpositie(bericht, sleutel):
#     bericht_arr = []
#     rij = []
#     encrypted_bericht = ""

#     for letter in bericht:
#         rij.append(letter)
#         if len(rij) % sleutel == 0:
#             bericht_arr.append(rij)
#             rij = []

#     if rij:
#         for i in range(sleutel-len(rij)):
#             rij.append("_")
#         bericht_arr.append(rij)

#     for rij in bericht_arr:
#         print(rij)

#     for i in range(len(bericht_arr[0])):
#         for rij in bericht_arr:
#             encrypted_bericht += rij[i]

#     return encrypted_bericht


# def decrypt_transpositie(encrypted_bericht, sleutel):
#     temp = encrypted_bericht
#     for j in range(len(encrypted_bericht) // sleutel):
#         decrypted_bericht = ""
#         bericht_arr = []
#         rij = []
#         for letter in temp:
#             rij.append(letter)
#             if len(rij) % sleutel == 0:
#                 bericht_arr.append(rij)
#                 rij = []

#         if rij:
#             for i in range(sleutel-len(rij)):
#                 rij.append(" ")
#             bericht_arr.append(rij)

#         for i in range(len(bericht_arr[0])):
#             for rij in bericht_arr:
#                 decrypted_bericht += rij[i]

#         temp = decrypted_bericht
#     return(temp)


def encrypt_transpositie(msg, key):
    cipher = ""

    # track key indices
    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # add the padding character '_' in empty
    # the empty cell of the matix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # create Matrix and insert message and
    # padding characters row-wise
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                          for row in matrix])
        k_indx += 1

    return cipher

# Decryption


def decrypt_transpositie(cipher, key):
    msg = ""

    # track key indices
    k_indx = 0

    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # convert key into list and sort
    # alphabetically so we can access
    # each character by its alphabetical position.
    key_lst = sorted(list(key))

    # create an empty matrix to
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # Arrange the matrix column wise according
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg


encrypted_bericht = encrypt_transpositie(bericht, sleutel)
print(encrypted_bericht)
decrypted_bericht = decrypt_transpositie(encrypted_bericht, sleutel)
print(decrypted_bericht)
