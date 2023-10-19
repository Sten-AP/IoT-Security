from broncode_modulaire_inverse import krijg_modulaire_inverse

def encrypt_affiene(bericht, a, b):
    encrypted_bericht = ""
    for char in bericht:
        if char.isalpha():
            if char.isupper():
                encrypted_bericht += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                encrypted_bericht += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
        else:
            encrypted_bericht += char
    return encrypted_bericht

def decrypt_affiene(encrypted_bericht, a, b):
    a_inv = krijg_modulaire_inverse(a, 26)
    if a_inv is None:
        return "Geen modulaire inverse"
    
    decrypted_bericht = ""
    for char in encrypted_bericht:
        if char.isalpha():
            if char.isupper():
                decrypted_bericht += chr((a_inv * (ord(char) - ord('A') - b)) % 26 + ord('A'))
            else:
                decrypted_bericht += chr((a_inv * (ord(char) - ord('a') - b)) % 26 + ord('a'))
        else:
            decrypted_bericht += char
    return decrypted_bericht