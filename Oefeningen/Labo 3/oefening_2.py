from oefening_1 import decrypt_caesar


def brute_force_caesar(encrypted_bericht, aantal_sleutels):
    for i in range(1, aantal_sleutels + 1):
        print(f"Sleutel: {i}\tBericht: {decrypt_caesar(encrypted_bericht, i)}")
