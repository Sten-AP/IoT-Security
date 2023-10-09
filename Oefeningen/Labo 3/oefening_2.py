from oefening_1 import encrypt, decrypt


def brute_force(encrypted_bericht, aantal_sleutels):
    for i in range(1, aantal_sleutels + 1):
        print(f"Sleutel: {i}\tBericht: {decrypt(encrypted_bericht, i)}")
