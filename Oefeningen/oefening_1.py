import random

ALFABET = "abcdefghijklmnopqrstuvwxyz"


def encrypt_caesar(bericht, sleutel):
    encrypted_bericht = ""
    for let in bericht:
        encrypted_bericht += ALFABET[(ALFABET.find(let) +
                                      sleutel) % len(ALFABET)]
    return encrypted_bericht


def decrypt_caesar(encrypted_bericht, sleutel):
    decrypted_bericht = ""
    for let in encrypted_bericht:
        decrypted_bericht += ALFABET[(ALFABET.find(let) -
                                      sleutel) % len(ALFABET)]
    return decrypted_bericht
