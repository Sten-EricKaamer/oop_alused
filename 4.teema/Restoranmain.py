from JäätiseKiosk import *


restoran1 = JäätiseKiosk("BabyBack Ribs", "Pizza 20€")
restoran2 = JäätiseKiosk("Timmu saiad", "Juustumaitseline Baguette 50€")
restoran3 = JäätiseKiosk("Burgerikuningas", "Jalasalat 5000€ ")


restoran1.restorani_kirjeldus()
restoran1.ava_restoran()

restoran2.restorani_kirjeldus()
restoran2.ava_restoran()

restoran3.restorani_kirjeldus()
restoran3.ava_restoran()

restoran1.maara_teenindatud_kylalised(123)

restoran2.maara_teenindatud_kylalised(13)
restoran2.suurenda_teenindatud_kylalised(155)

restoran1.näitajäätiseid()