"""
Pour cet exercice de code, vous allez réaliser un programme de type "minuteur" qui permettra d'afficher en temps réel le temps restant de cuisson.


-> Votre programme proposera 3 options :

- Oeufs à la coque : 3 minutes

- Oeufs mollets : 6 minutes

- Oeufs durs : 9 minutes


Une fois l'option choisie, votre programme commencera à attendre la durée concernée.

A chaque seconde, vous afficherez un "." sur une même ligne (afin que l'on voit un effet de progression).

Et toutes les 10 secondes vous irez à la ligne suivante en affichant le temps restant.

    d = 100
    min = d//60 # division entière (pas de virgules)
    sec = d-min*60
"""
import time
import platform
import winsound

ONE_MINUTE_IN_SECONDS = 60


# affichage des options de cuisson des oeufs
print("a - Oeufs à la coque : 3 minutes ")
print("b - Oeufs mollets : 6 minutes")
print("c - Oeufs durs : 9 minutes")
choice = input("Votre choix :")


# créer le timeur
def timeur(minutes_to_seconds):
    for i in range(minutes_to_seconds, 0, -10):
    # convertir les secondes en minutes
        minutes_timer = i // 60
        #print(minutes_timer)
    # récupérer les secondes restantes
        secondes_timer = i - minutes_timer * 60
        #print(secondes_timer)
         # afficher le timer complet
        print(f"\n Temps restant : {minutes_timer}: {secondes_timer}")
    # afficher les secondes restantes, toutes les 10s. Marquer chaque seconde écoulée par un .
        for j in range(10):
            time.sleep(1)
            print(".", end="", flush=True)


# récupérer l'option choisie par l'user
if choice == "a":
    minutes_to_seconds = 3 * ONE_MINUTE_IN_SECONDS
    timeur(minutes_to_seconds)
elif choice == "b":
    minutes_to_seconds =  6 * ONE_MINUTE_IN_SECONDS
    timeur(minutes_to_seconds)
elif choice == "c":
    minutes_to_seconds = 9 * ONE_MINUTE_IN_SECONDS
    timeur(minutes_to_seconds)
else: 
    print("ERREUR: Vous ne pouvez rentrer que a, b ou c en minuscules")


print("\n")
print("Cuisson terminée !")

if platform.system() == "Windows":
 
    # Tu peux varier la féquence (aigue -> grave)
    frequency = 500
    duration = 500
    winsound.Beep(frequency, duration)

# Si le script n'est pas exécuté sous windows 
else:
    print("Driiiiiiiiiiiing!!!")

