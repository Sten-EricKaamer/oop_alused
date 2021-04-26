from oppimine import *

aineteemad = Andmed("OOP põhimõtted", "Klassid ja Objektid", "Konstruktor")
print("Aine teemad: ")
for teema in aineteemad:
    print("* " + teema)

Tim = Opilane("Tim")
Lisette = Opilane("Lisette")
Anna = Opetaja("Anna")

Tim.kirjeldus()
Tim.opib(aineteemad[0])
Tim.kirjeldus()

Anna.opetab(aineteemad[1], Tim, Lisette)
Lisette.kirjeldus()
Tim.kirjeldus()

print("UNUSTAMISE TEST")
print("Tim unustab ära " + aineteemad[1])
Tim.unutab(aineteemad[1])
Tim.kirjeldus()