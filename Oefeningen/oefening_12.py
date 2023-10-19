ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SUBSTITUTIE = "QWERTYUIOPASDFGHJKLZXCVBNM"

def substitutiesleutel(alfabet, substitutie):
    if len(alfabet) != len(substitutie):
        raise ValueError("Alfabet en subsitutie zijn niet even lang.")
    
    sleutel = {}
    for i in range(len(alfabet)):
        sleutel[alfabet[i]] = substitutie[i]
    
    return sleutel

def encrypt_substitutie(bericht, substitutie_key):
    encrypted_bericht = ""
    for char in bericht:
        if char in substitutie_key:
            encrypted_bericht += substitutie_key[char]
        else:
            encrypted_bericht += char
    return encrypted_bericht

def decrypt_substitutie(encrypted_bericht, substitutie_key):
    decryption_sleutel = {v: s for s, v in substitutie_key.items()}
    decrypted_bericht = ""
    for char in encrypted_bericht:
        if char in decryption_sleutel:
            decrypted_bericht += decryption_sleutel[char]
        else:
            decrypted_bericht += char
    return decrypted_bericht


substitutie_key = substitutiesleutel(ALFABET, SUBSTITUTIE)
bericht = "CODE"

encrypted_bericht = encrypt_substitutie(bericht, substitutie_key)
print(encrypted_bericht)

decrypted_bericht = decrypt_substitutie(encrypted_bericht, substitutie_key)
print(decrypted_bericht)
