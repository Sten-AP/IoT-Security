from broncode_modulaire_inverse import ggd, krijg_modulaire_inverse


ALFABET = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+1234567890-= |[]\\:\";'<>?,./~`ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ALFABET = "abcdefghijklmnopqrstuvwxyz"
sleutel = 7
bericht = "HELLO WORLD"


def encrypt_caesar(bericht, sleutel):
    encrypted_bericht = ""
    for let in bericht:
        encrypted_bericht += ALFABET[(ALFABET.find(let)
                                      * sleutel) % len(ALFABET)]
    return encrypted_bericht


def decrypt_caesar(encrypted_bericht, sleutel):
    decrypted_bericht = ""
    for let in encrypted_bericht:
        decrypted_bericht += ALFABET[(ALFABET.find(
            let) * krijg_modulaire_inverse(sleutel, len(ALFABET))) % len(ALFABET)]
    return decrypted_bericht


print(encrypt_caesar(bericht, sleutel))
print(decrypt_caesar(encrypt_caesar(bericht, sleutel), sleutel))
