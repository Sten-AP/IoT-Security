from broncode_modulaire_inverse import krijg_modulaire_inverse


ALFABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

def encrypt_x_versleuteling(bericht, sleutel):
    encrypted_bericht = ""
    for let in bericht:
        letter = ALFABET.find(let) * sleutel % len(ALFABET)
        encrypted_bericht += ALFABET[letter]
    return encrypted_bericht


def decrypt_x_versleuteling(encrypted_bericht, sleutel):
    decrypted_bericht = ""
    for let in encrypted_bericht:
        letter = ALFABET.find(let) * krijg_modulaire_inverse(sleutel, len(ALFABET)) % len(ALFABET)
        decrypted_bericht += ALFABET[letter]
    return decrypted_bericht

