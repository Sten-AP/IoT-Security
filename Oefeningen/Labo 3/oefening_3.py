import math


def encrypt_transpositie(bericht, sleutel):
    encrypted_bericht = ""

    msg_len = float(len(bericht))
    msg_lst = list(bericht)

    row = int(math.ceil(msg_len / sleutel))

    fill_null = int((row * sleutel) - msg_len)
    msg_lst.extend('_' * fill_null)

    matrix = [msg_lst[i: i + sleutel]
              for i in range(0, len(msg_lst), sleutel)]

    for _ in range(sleutel):
        encrypted_bericht += ''.join([row[_]
                                      for row in matrix])

    return encrypted_bericht
