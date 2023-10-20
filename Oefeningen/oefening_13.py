def decrypt_substitution_hack(encrypted_bericht):
    common_letters = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    substitution_key = {}

    encrypted_letters = [char for char in encrypted_bericht if char.isalpha()]
    encrypted_letter_count = {char: encrypted_letters.count(char) for char in set(encrypted_letters)}
    sorted_encrypted_letters = sorted(encrypted_letter_count, key=lambda char: -encrypted_letter_count[char])
    
    for i in range(min(len(common_letters), len(sorted_encrypted_letters))):
        substitution_key[sorted_encrypted_letters[i]] = common_letters[i]
    
    decrypted_bericht = ""
    for char in encrypted_bericht:
        if char in substitution_key:
            decrypted_bericht += substitution_key[char]
        else:
            decrypted_bericht += char
    
    return decrypted_bericht

encrypted_bericht = "YFJ YMJKJ WJYFJ YFYJ KJYFJ E"

decrypted_bericht = decrypt_substitution_hack(encrypted_bericht)
print(decrypted_bericht)
