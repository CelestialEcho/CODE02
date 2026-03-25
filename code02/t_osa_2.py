"""
lista = ["kissa", "koira", "gerbiili"]
for sana in lista:
    print(sana)
"""

"""
lista = ["kissa", "koira", "gerbiili"]

def onko_alkukirjain_k(sana):
    return sana[0] == "k"

for sana in lista:
    if onko_alkukirjain_k(sana):
        print(sana)
"""

"""
tiedosto = open("nimi.txt", "w", encoding='UTF-8')
tiedosto.write("Matti Meikäläine")
tiedosto.close()
"""

"""
tiedosto = open("neliöt.txt", "w", encoding='UTF-8')
for i in range(1, 101):
    tiedosto.write(str(i**2) + "\n")
tiedosto.close()
"""

"""
tiedosto = open("lyhyt_kirja.txt", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

print(rivit[2])

for rivi in rivit:
    print(rivi)
"""
"""
tiedosto = open("kotus_sanat.txt", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

for sana in rivit:
    sana = sana.rstrip()
    if len(sana) == 3:
        print(sana)
"""
"""
tiedosto = open("kotus_sanat.txt", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

for sana in rivit:
    sana = sana.rstrip()
    if sana[-3:] == "ari":
        print(sana)

"""
"""
tiedosto = open("kotus_sanat.txt", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

for sana in rivit:
    sana = sana.rstrip()
    if sana == sana[::-1] and len(sana) > 1:
        print(sana)
"""
"""
tiedosto = open("kotus_sanat.txt", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

sanat = []
for sana in rivit:
    sanat.append(sana.rstrip())

for sana in sanat:
    peili = sana[::-1]
    if peili in sanat and peili != sana:
        print(sana, "->", peili)
"""

"""
tiedosto = open("kotus_sanat.txt", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

for sana in rivit:
    sana = sana.rstrip()
    aakkosjärjestyksessä = True
    for i in range(len(sana) - 1):
        if sana[i] > sana[i+1]:
            aakkosjärjestyksessä = False
    if aakkosjärjestyksessä:
        print(sana)
"""

"""
tiedosto = open("Seitsemän_veljestä.txt", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

määrä = 0
for rivi in rivit:
    sanat = rivi.split()
    for sana in sanat:
        sana = sana.lower().strip(".,!?")
        if sana == "juhani":
            määrä += 1

print("Juhani mainitaan " + str(määrä) + " kertaa.")
"""

"""
tiedosto = open("Seitsemän_veljestä.txt", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

veljekset = ["juhani", "tuomas", "aapo", "simeoni", "timo", "lauri", "eero"]
maininnat = {}
for veli in veljekset:
    maininnat[veli] = 0

for rivi in rivit:
    sanat = rivi.split()
    for sana in sanat:
        sana = sana.lower().strip(".,!?")
        if sana in maininnat:
            maininnat[sana] += 1

for veli in maininnat:
    print(veli + ": " + str(maininnat[veli]) + " kertaa")
"""

"""
tiedosto = open("seitseman_veljesta", "r", encoding='UTF-8')
rivit = tiedosto.readlines()
tiedosto.close()

sanamäärät = {}
for rivi in rivit:
    sanat = rivi.split()
    for sana in sanat:
        sana = sana.lower().strip(".,!?;:")
        if sana != "":
            if sana in sanamäärät:
                sanamäärät[sana] += 1
            else:
                sanamäärät[sana] = 1

järjestetty = sorted(sanamäärät, key=sanamäärät.get, reverse=True)
for sana in järjestetty[:100]:
    print(sana + ": " + str(sanamäärät[sana]))
"""