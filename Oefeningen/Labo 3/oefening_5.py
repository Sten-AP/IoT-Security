from oefening_3 import encrypt_transpositie
from oefening_4 import decrypt_transpositie
import time
sleutel = 3
file = open('Oefeningen\Labo 3\woordenlijst.txt', 'r')
encrypted_file = open('Oefeningen\Labo 3\encrypted_woordenlijst.txt', 'w')
decrypted_file = open('Oefeningen\Labo 3\decrypted_woordenlijst.txt', 'w')

for woord in file:
    encrypted_file.write(encrypt_transpositie(woord, sleutel))

encrypted_file = open('Oefeningen\Labo 3\encrypted_woordenlijst.txt', 'r')

for woord in encrypted_file:
    decrypted_file.write(decrypt_transpositie(woord, sleutel))
