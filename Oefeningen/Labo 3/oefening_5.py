from oefening_3 import encrypt_transpositie
from oefening_4 import decrypt_transpositie

sleutel = 5

file = open('Labo 3/woordenlijst.txt', 'r')
encrypted_file = open('Labo 3/encrypted_woordenlijst.txt', 'w')

for woord in file.readlines():
    encrypted_file.write(encrypt_transpositie(woord[:-1], sleutel) + "\n")

encrypted_file = open('Labo 3/encrypted_woordenlijst.txt', 'r')
decrypted_file = open('Labo 3/decrypted_woordenlijst.txt', 'w')

for woord in encrypted_file.readlines():
    decrypted_file.write(decrypt_transpositie(woord[:-1], sleutel) + "\n")
