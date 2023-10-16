def ggd(a, b):
    # Geeft de grootste gemene deler terug
    while a != 0:
        a, b = b % a, a
    return b


def krijg_modulaire_inverse(a, m):
    # Geeft de modulaire inverse terug van a % m, die gelijk is
    # aan het getal x zodat a*x % m = 1

    if ggd(a, m) != 1:
        return None  # Er bestaat geen modulaire inverse als a & m geen relatieve priemgetallen zijn

    # Bereken gebruik makend van het zgn uitgebreide Euclidische algoritme
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # geeft het "gehele" quotiënt terug
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


print(f"7 % 4 = {6%4}")
print(f"Modulaire inverse x zodat 7*x % 2... x = {krijg_modulaire_inverse(7,4)}")
