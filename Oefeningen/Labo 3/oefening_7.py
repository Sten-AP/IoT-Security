from oefening_3 import encrypt_transpositie
from oefening_4 import decrypt_transpositie

bericht = "Deze zin is zometeen niet te lezen"
sleutel = 5

nederlandse_woorden_file = open("Labo 3\woordenlijst.txt", "r")
nederlandse_woorden = []
for woord in nederlandse_woorden_file:
    nederlandse_woorden.append(woord)


def brute_force_transpositie(encrypted_bericht, aantal_sleutels):
    for i in range(1, aantal_sleutels + 1):
        decrypted_woord = decrypt_transpositie(encrypted_bericht, i)
        print(f"Sleutel: {i}\tBericht: {decrypted_woord}")
        woorden = decrypted_woord.split(" ")
        print(woorden)
        for nederlands_woord in nederlandse_woorden:
            if nederlands_woord in woorden:
                print(nederlands_woord in woorden)

    return decrypted_woord


encrypted_bericht = encrypt_transpositie(bericht, sleutel)
forced_decrypted_bericht = brute_force_transpositie(encrypted_bericht, 10)
print(forced_decrypted_bericht)
