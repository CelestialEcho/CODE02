"""
nimi = input("Anna nimesi: ")
ika = int(input("Anna ikäsi: "))

syntymavuosi = 2026 - ika
sekunnit = ika * 365 * 24 * 60 * 60

print("Hei", nimi)
print("Syntymävuosi:", syntymavuosi)
print("Olet elänyt noin", sekunnit, "sekuntia")
"""

"""
import math

a = float(input("Anna sivu a: "))
b = float(input("Anna sivu b: "))

c = math.sqrt(a**2 + b**2)

print("Hypotenuusa on:", c)
"""

"""
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))

print("Summa:", luku1 + luku2)
print("Erotus:", luku1 - luku2)
print("Tulo:", luku1 * luku2)

if luku2 != 0:
    print("Osamäärä:", luku1 / luku2)
else:
    print("Nollalla ei voi jakaa")
"""

"""
luku = int(input("Anna luku: "))

if luku % 2 == 0:
    print("Parillinen")
else:
    print("Pariton")
"""

"""
sana = input("Anna sana: ")

if len(sana) > 1:
    print("Merkkien määrä:", len(sana))
"""

"""
hinta = float(input("Työpaikkaruoan hinta: "))
maara = int(input("Kuinka monta kertaa viikossa: "))
muut = float(input("Muut ruokakulut viikossa: "))

viikko = hinta * maara + muut

if viikko > 100:
    viikko *= 0.9

paiva = viikko / 7

print("Viikkokulut:", viikko)
print("Päiväkulut:", paiva)
"""

"""
nimi1 = input("Ensimmäisen nimi: ")
vuosi1 = int(input("Syntymävuosi: "))

nimi2 = input("Toisen nimi: ")
vuosi2 = int(input("Syntymävuosi: "))

if vuosi1 < vuosi2:
    print(nimi1, "on vanhempi")
elif vuosi2 < vuosi1:
    print(nimi2, "on vanhempi")
else:
    print("He ovat samanikäisiä")
"""

"""
luku = int(input("Anna luku: "))

if 4 <= luku <= 9:
    print("Luku on välillä 4 ja 9")
else:
    print("Luku ei ole välillä 4 ja 9")
"""

"""
luku = int(input("Anna luku: "))

if luku % 3 == 0 and luku % 5 == 0:
    print("FizzBuzz")
elif luku % 3 == 0:
    print("Fizz")
elif luku % 5 == 0:
    print("Buzz")
"""

"""
pisteet = int(input("Anna pistemäärä (0-100): "))

if 90 <= pisteet <= 100:
    print("Erinomainen")
elif 75 <= pisteet <= 89:
    print("Hyvä")
elif 60 <= pisteet <= 74:
    print("Tyydyttävä")
else:
    print("Hylätty")
"""

"""
a = int(input("Anna luku 1: "))
b = int(input("Anna luku 2: "))
c = int(input("Anna luku 3: "))

luvut = [a, b, c]
luvut.sort()

print("Järjestyksessä:", luvut)
"""

"""
import random

a = random.randint(1, 10)
b = random.randint(1, 10)

operaatio = random.choice(["+", "-", "*", "/"])

if operaatio == "+":
    oikea = a + b
elif operaatio == "-":
    oikea = a - b
elif operaatio == "*":
    oikea = a * b
else:
    oikea = a / b

vastaus = float(input(f"{a} {operaatio} {b} = "))

if vastaus == oikea:
    print("Oikein!")
else:
    print("Väärin, oikea vastaus oli", oikea)
"""

"""
luku = -1

while luku <= 0:
    luku = int(input("Anna positiivinen luku: "))
"""

"""
oikea = "salasana"
yritykset = 0

while yritykset < 3:
    s = input("Anna salasana: ")
    
    if s == oikea:
        print("Oikein!")
        break
    else:
        print("Väärin")
    
    yritykset += 1

if yritykset == 3:
    print("Liikaa yrityksiä")
"""

"""
while True:
    a = int(input("Anna luku: "))
    b = int(input("Anna toinen luku: "))
    print("Summa:", a + b)
"""

"""
N = int(input("Anna positiivinen luku: "))

for i in range(-N, N + 1):
    if i != 0:
        print(i)
"""

"""
summa = 0

for i in range(1, 101):
    summa += i

print("Summa:", summa)
"""

"""
import random

kierrokset = int(input("Kuinka monta kierrosta: "))

voitto1 = 0
voitto2 = 0
tasapeli = 0

for i in range(kierrokset):
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)

    if n1 > n2:
        voitto1 += 1
    elif n2 > n1:
        voitto2 += 1
    else:
        tasapeli += 1

print("Noppa1 voitti:", voitto1)
print("Noppa2 voitti:", voitto2)
print("Tasapelit:", tasapeli)
"""

"""
import random

oikea = random.randint(1, 100)
yritykset = 0

while True:
    arvaus = int(input("Arvaa luku: "))
    yritykset += 1

    if arvaus == oikea:
        print("Onneksi olkoon! Yrityksiä:", yritykset)
        break
    elif arvaus < oikea:
        print("Suurempi")
    else:
        print("Pienempi")
"""

"""
sana = input("Anna sana: ")
maara = 0

for kirjain in sana:
    if kirjain == "a":
        maara += 1

print("A-kirjaimia:", maara)
"""

"""
alku = int(input("Alku: "))
loppu = int(input("Loppu: "))

for i in range(alku, loppu + 1):
    if i % 2 != 0:
        print(i)
"""

"""
luku = int(input("Anna luku: "))

on_alkuluku = True

if luku < 2:
    on_alkuluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break

if on_alkuluku:
    print("Alkuluku")
else:
    print("Ei alkuluku")
"""