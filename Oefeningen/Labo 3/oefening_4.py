import math


def decrypt_transpositie(encrypted_bericht, sleutel):
    decrypted_bericht = ""

    msg_indx = 0
    msg_len = float(len(encrypted_bericht))
    msg_lst = list(encrypted_bericht)

    row = int(math.ceil(msg_len / sleutel))

    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * sleutel]

    for _ in range(sleutel):
        for j in range(row):
            dec_cipher[j][_] = msg_lst[msg_indx]
            msg_indx += 1

    try:
        decrypted_bericht = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = decrypted_bericht.count('_')

    if null_count > 0:
        return decrypted_bericht[: -null_count]

    return decrypted_bericht
