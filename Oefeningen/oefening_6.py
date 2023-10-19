from oefening_1 import decrypt_caesar


def brute_force_caesar_met_nederlands(encrypted_bericht, aantal_sleutels):
    nederlandse_woorden_file = open("woordenlijst.txt", "r").readlines()
    for i in range(1, aantal_sleutels + 1):
        decrypted_woord = decrypt_caesar(encrypted_bericht, i)
        print(f"Sleutel: {i}\tBericht: {decrypted_woord}")
        woorden = decrypted_woord.split(" ")
        for nederlands_woord in nederlandse_woorden_file:
            if nederlands_woord[:-1] in woorden and len(nederlands_woord[:-1]) > 4:
                return decrypted_woord

