import time

# 1ere chose a faire :afficher le menu de cuisson des oeufs
print("Cuisson des oeufs")
print("1 - Oeufs à la coque : 3 minutes")
print("2 - Oeufs à la coque : 6 minutes")
print("3 - Oeufs à la coque : 9 minutes")
choix = input("Votre choix: ")

duree = 0
if choix == "1":
    duree = 3 * 60
if choix == "2":
    duree = 6 * 60
if choix == "3":
    duree = 9 * 60


# Ne sachant pas encore sur quelle condition bouclée, on commence la réflexion algorithmique 
# avec while True:

while True:
    time.sleep(1)
    print(".", end="", flush=True)