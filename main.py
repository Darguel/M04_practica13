from Ejercicio_A import animal as am
from Ejercicio_A import vehicle as vc
from Ejercicio_A import school as sc

gato = am.animal("mishu", "2", "mamifero", "felino", "4", "si")
gato.salutacio()
gato.setEdad("3")
gato.salutacio()

lagarto = am.animal("dragoncito", "4", "reptil", "lagarto", "4", "si")
lagarto.salutacio()
lagarto.setEdad("5")
lagarto.salutacio()

coche = vc.vehicle("bmw", "2", "4", "coche", "4", "no")
coche.salutacio()
coche.setTuneado("si")
coche.salutacio()

moto = vc.vehicle("yamaha", "3", "0", "moto", "2", "no")
moto.salutacio()
moto.setAños("3")
moto.salutacio()

carlit = sc.school("3", "9", "300", "publico", "1", "667654587")
carlit.salutacio()
carlit.setAulas("10")
carlit.salutacio()

balmes = sc.school("4", "45", "1200", "publico", "2", "6687834894")
balmes.salutacio()
balmes.setAulas("10")
balmes.salutacio()