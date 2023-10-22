ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
SUBSTITUTIE = "QWERTYUIOPASDFGHJKLZXCVBNM qwertyuiopasdfghjklzxcvbnm"

def substitutiesleutel(alfabet, subsitutie):
    if len(alfabet) != len(subsitutie):
        raise ValueError("Alfabet en subsitutie zijn niet even lang.")
    
    sleutel = {}
    for i in range(len(alfabet)):
        sleutel[alfabet[i]] = SUBSTITUTIE[i]
    return sleutel

def decrypt_substitutie(bericht, sleutel):
    encrypted_bericht = ""
    for char in bericht:
        if char in sleutel:
            encrypted_bericht += sleutel[char]
        else:
            encrypted_bericht += char
    return encrypted_bericht

def encrypt_substitutie(encrypted_bericht, sleutel):
    decrypted_sleutel = {v: s for s, v in sleutel.items()}
    decrypted_bericht = ""
    for char in encrypted_bericht:
        if char in decrypted_sleutel:
            decrypted_bericht += decrypted_sleutel[char]
        else:
            decrypted_bericht += char
    return decrypted_bericht