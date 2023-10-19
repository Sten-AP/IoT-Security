from oefening_8 import decrypt_x_versleuteling
 
def brute_force_x_versleuteling(encrypted_bericht, aantal_sleutels):
    nederlandse_woorden_file = open("woordenlijst.txt", "r").readlines()
    for i in range(1, aantal_sleutels + 1):
        decrypted_woord = decrypt_x_versleuteling(encrypted_bericht, i)
        print(f"Sleutel: {i}\tBericht: {decrypted_woord}")
        woorden = decrypted_woord.split(" ")
        for nederlands_woord in nederlandse_woorden_file:
            if nederlands_woord[:-1] in woorden and len(nederlands_woord[:-1]) > 4:
                return decrypted_woord
