from oefening_1 import encrypt_caesar, decrypt_caesar
from oefening_2 import brute_force_caesar

BERICHT = "Ik ben in het nederlands geschreven."
SLEUTEL = 30


def detect_nederlands(decrypted_bericht):
    file = open('Labo 3/woordenlijst.txt', 'r')

    for woord in file.readlines():
        if woord[:-1] in decrypted_bericht and len(woord[:-1]) > 4:
            print(f"Nederlands gevonden: {decrypted_bericht}")
            return True
    return False


def brute_force_caesar_met_nederlands(encrypted_bericht, aantal_sleutels):
    for i in range(1, aantal_sleutels + 1):
        print(f"Sleutel: {i}\tBericht: {decrypt_caesar(encrypted_bericht, i)}")
        nederlands = detect_nederlands(decrypt_caesar(encrypted_bericht, i))
        if nederlands:
            break


encrypted_bericht = encrypt_caesar(BERICHT, SLEUTEL)
decrypted_bericht = brute_force_caesar_met_nederlands(encrypted_bericht, 200)
