import random

alfabet = list(
    "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+1234567890-= |[]\\:\";'<>?,./~`ABCDEFGHIJKLMNOPQRSTUVWXYZ")
random.shuffle(alfabet)
ALFABET = "".join(alfabet)


def encrypt(bericht, sleutel):
    encrypted_bericht = ""
    for let in bericht:
        encrypted_bericht += ALFABET[(ALFABET.find(let) +
                                      sleutel) % len(ALFABET)]
    return encrypted_bericht


def decrypt(encrypted_bericht, sleutel):
    decrypted_bericht = ""
    for let in encrypted_bericht:
        decrypted_bericht += ALFABET[(ALFABET.find(let) -
                                      sleutel) % len(ALFABET)]
    return decrypted_bericht
