from oefening_1 import encrypt, decrypt
from oefening_2 import brute_force
import pandas as pd
import numpy as np

sleutel = 3
bericht = "HELLOWORLD"

bericht_in_rijen = []
rij = []

for letter in bericht:
    rij.append(letter)
    if len(rij) % sleutel == 0:
        bericht_in_rijen.append(rij)
        rij = []
if rij:
    for i in range(sleutel-len(rij)):
        rij.append(" ")
    bericht_in_rijen.append(rij)

transposed_df = df.transpose()


# print(bericht_in_rijen)
