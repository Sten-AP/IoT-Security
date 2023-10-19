from broncode_modulaire_inverse import krijg_modulaire_inverse
from oefening_10 import encrypt_affiene, decrypt_affiene

a = 5
b = 8
bericht = "deze zin werd versleuteld"

def brute_force_affiene(encrypted_bericht):
    nederlandse_woorden_file = open("Oefeningen\woordenlijst.txt", "r").readlines()
    alfabet = 26
    for a in range(1, alfabet):
        for b in range(alfabet):
            if krijg_modulaire_inverse(a, alfabet) is None:
                continue
         
            decrypted_woord = decrypt_affiene(encrypted_bericht, a, b)
            print(f"Sleutel (a={a}, b={b}): {decrypted_woord}")
            woorden = decrypted_woord.split(" ")
            for nederlands_woord in nederlandse_woorden_file:
            	if nederlands_woord[:-1] in woorden and len(nederlands_woord[:-1]) > 4:
                	return decrypted_woord
					




encrypted_bericht = encrypt_affiene(bericht, a, b)
print(encrypted_bericht)
decrypted_bericht = brute_force_affiene(encrypted_bericht)
print(decrypted_bericht)
