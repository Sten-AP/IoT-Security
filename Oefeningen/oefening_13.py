from oefening_12 import encrypt_substitutie, decrypt_substitutie, substitutiesleutel

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
SUBSTITUTIE = "QWERTYUIOPASDFGHJKLZXCVBNM qwertyuiopasdfghjklzxcvbnm"

def decrypt_substitution_hack(encrypted_bericht):
    # common_letters = "ETAOINSHRDLCUMWFGYPBVKJXQZ etaoinshrdlcumwfgyobvkjxqz"
    common_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"

    substitution_key = {}

    encrypted_letters = [char for char in encrypted_bericht if char.isalpha()]
    encrypted_letter_count = {char: encrypted_letters.count(char) for char in set(encrypted_letters)}
    sorted_encrypted_letters = sorted(encrypted_letter_count, key=lambda char: -encrypted_letter_count[char])
    
    for i in range(min(len(common_letters), len(sorted_encrypted_letters))):
        substitution_key[sorted_encrypted_letters[i]] = common_letters[i]
    
    return decrypt_substitutie(encrypted_bericht, substitution_key)


sleutel = substitutiesleutel(ALFABET, SUBSTITUTIE)
bericht = "deze zin wordt versleuteld"

encrypted_bericht = encrypt_substitutie(bericht, sleutel)
print(encrypted_bericht)

decrypted_bericht = decrypt_substitutie(encrypted_bericht, sleutel)
print(decrypted_bericht)

decrypted_bericht = decrypt_substitution_hack(encrypted_bericht)
print(decrypted_bericht)
