from kasutaja import *

kasutaja = Kasutaja("Timmu", "Õunapuu","timmu.ounapuu","qwerty")
administraator = Admin("Tõnu","Januvere","tonu.januvere","QWERTY")

kasutaja.kirjelda_kasutajat("Workgroup")
administraator.kirjelda_kasutajat("Workgroup")
administraator.privileegid.show_privileges()


#kasutaja1 = Privileegid("Timmu","Õunapuu")
#kasutaja2 = Privileegid("Oliver","Mõttus")
#kasutaja3 = Privileegid("Joonatan","Kelder")

#kasutaja1.set_privileeg("root")
#kasutaja2.set_privileeg("user")
#kasutaja3.set_privileeg("user")

#kasutaja1.set_domain("Domeen")
#kasutaja2.set_domain("Domeen 2.0")
#kasutaja3.set_domain("WorkGroup 3.0")


#kasutaja1.kirjelda_kasutajat(kasutaja1.get_domain(),kasutaja1.get_privileeg())
#kasutaja2.kirjelda_kasutajat(kasutaja2.get_domain(),kasutaja2.get_privileeg())
#kasutaja3.kirjelda_kasutajat(kasutaja3.get_domain(),kasutaja3.get_privileeg())

#kasutaja1.privileegid.show_privileges()
#kasutaja2.privileegid.show_privileges()
#kasutaja3.privileegid.show_privileges()