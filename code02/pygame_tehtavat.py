import pygame
import random

"""
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
w = robo.get_width()
h = robo.get_height()

ikkuna.fill((25, 25, 25))
ikkuna.blit(robo, (0, 0))
ikkuna.blit(robo, (640 - w, 0))
ikkuna.blit(robo, (0, 480 - h))
ikkuna.blit(robo, (640 - w, 480 - h))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()
"""
"""
# Tehtävä 3: kymmenen robottia riviin
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
w = robo.get_width()

ikkuna.fill((25, 25, 25))
for i in range(10):
    ikkuna.blit(robo, (i * w, 0))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()
"""


"""
# Tehtävä 4: sata robottia, 10 riviä, 10 per rivi
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
w = robo.get_width()
h = robo.get_height()

ikkuna.fill((25, 25, 25))
for rivi in range(10):
    for sarake in range(10):
        ikkuna.blit(robo, (sarake * w + (rivi * 1.1), rivi * (h / 5)))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()
"""


"""
# Tehtävä 5: tuhat robottia satunnaisiin paikkoihin
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
w = robo.get_width()
h = robo.get_height()

ikkuna.fill((25, 25, 25))
for _ in range(1000):
    x = random.randint(0, 640 - w)
    y = random.randint(0, 480 - h)
    ikkuna.blit(robo, (x, y))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()
"""

"""
# Tehtävä 6: robotti liikkuu ylhäältä alas
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()

x = 300
y = 0

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()

    ikkuna.fill((25, 25, 25))
    ikkuna.blit(robo, (x, y))
    pygame.display.flip()

    y += 2
    if y > 480:
        y = 0

    kello.tick(60)
"""

"""
# Tehtävä 7: robotti törmää seiniin ja vaihtaa suuntaa
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()
w = robo.get_width()
h = robo.get_height()

x = 0
y = 0
dx = 2
dy = 2

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()

    ikkuna.fill((25, 25, 25))
    ikkuna.blit(robo, (x, y))
    pygame.display.flip()

    x += dx
    y += dy

    if x <= 0 or x >= 640 - w:
        dx = -dx
    if y <= 0 or y >= 480 - h:
        dy = -dy

    kello.tick(60)
"""

"""
# Tehtävä 8: robotti kiertää ikkunan reunoja
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()
w = robo.get_width()
h = robo.get_height()

x = 0
y = 0
suunta = "oikea"

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()

    ikkuna.fill((25, 25, 25))
    ikkuna.blit(robo, (x, y))
    pygame.display.flip()

    if suunta == "oikea":
        x += 2
        if x >= 640 - w:
            suunta = "alas"
    elif suunta == "alas":
        y += 2
        if y >= 480 - h:
            suunta = "vasen"
    elif suunta == "vasen":
        x -= 2
        if x <= 0:
            suunta = "ylös"
    elif suunta == "ylös":
        y -= 2
        if y <= 0:
            suunta = "oikea"

    kello.tick(60)
"""

"""
# Tehtävä 9: kolme robottia eri nopeuksilla, törmäävät seiniin
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()
w = robo.get_width()
h = robo.get_height()

robotit = [
    [0,   100, 2, 1],
    [0,   200, 3, 2],
    [0,   300, 5, 3],
]

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()

    ikkuna.fill((25, 25, 25))
    for robo_tiedot in robotit:
        x, y, dx, dy = robo_tiedot
        ikkuna.blit(robo, (x, y))
        robo_tiedot[0] += dx
        robo_tiedot[1] += dy
        if robo_tiedot[0] <= 0 or robo_tiedot[0] >= 640 - w:
            robo_tiedot[2] = -robo_tiedot[2]
        if robo_tiedot[1] <= 0 or robo_tiedot[1] >= 480 - h:
            robo_tiedot[3] = -robo_tiedot[3]

    pygame.display.flip()
    kello.tick(60)
"""

"""
# Tehtävä 10: robotti-invaasio
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
robo = pygame.image.load("robo.png")
kello = pygame.time.Clock()
w = robo.get_width()
h = robo.get_height()

robotit = []

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()

    if random.randint(1, 30) == 1:
        x = random.randint(0, 640 - w)
        robotit.append([x, -h, 0, 3])

    ikkuna.fill((25, 25, 25))

    uudet = []
    for r in robotit:
        ikkuna.blit(robo, (r[0], r[1]))
        r[0] += r[2]
        r[1] += r[3]

        if r[1] >= 480 - h and r[2] == 0:
            r[2] = random.choice([-3, 3])
            r[3] = 0

        if -w <= r[0] <= 640:
            uudet.append(r)

    robotit = uudet

    pygame.display.flip()
    kello.tick(60)
"""

"""
# Tehtävä 11: pomppiva DVD-logo
pygame.init()
ikkuna = pygame.display.set_mode((640, 480))
logo = pygame.image.load("dvd.png")
kello = pygame.time.Clock()
w = logo.get_width()
h = logo.get_height()

x = 100
y = 100
dx = 3
dy = 2

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            exit()

    ikkuna.fill((0, 0, 0))
    ikkuna.blit(logo, (x, y))
    pygame.display.flip()

    x += dx
    y += dy

    if x <= 0 or x >= 640 - w:
        dx = -dx
    if y <= 0 or y >= 480 - h:
        dy = -dy

    kello.tick(60)
"""