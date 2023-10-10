sleutel = 4
bericht = "HELLOWORLD"


def encrypt_transpositie(bericht, sleutel):
    bericht_arr = []
    rij = []
    for letter in bericht:
        rij.append(letter)
        if len(rij) % sleutel == 0:
            bericht_arr.append(rij)
            rij = []
    if rij:
        for i in range(sleutel-len(rij)):
            rij.append(" ")
        bericht_arr.append(rij)

    encrypted_bericht = ""
    for i in range(len(bericht_arr[0])):
        for rij in bericht_arr:
            # if rij[i] != " ":
            encrypted_bericht += rij[i]
    return encrypted_bericht


def decrypt_transpositie(encrypted_bericht, sleutel):
    decrypted_bericht = ""
    rij = []
    rij.append(encrypted_bericht[0])
    rij.append(encrypted_bericht[3])
    rij.append(encrypted_bericht[6])
    print(rij)

    # if rij:
    #     for i in range(sleutel-len(rij)):
    #         rij.append(" ")
    # print(rij)


encrypted_bericht = encrypt_transpositie(bericht, sleutel)
print(encrypted_bericht)
decrypted_bericht = decrypt_transpositie(encrypted_bericht, sleutel)
# print(decrypted_bericht)
