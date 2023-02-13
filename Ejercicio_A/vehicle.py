class vehicle:
    def __init__(self, marca, años, puertas, tipo, ruedas, tuneado):
        self.marca = marca
        self.años = años
        self.puertas = puertas
        self.tipo = tipo
        self.ruedas = ruedas
        self.tuneado = tuneado

    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    def getAños(self):
        return self.años
    def setAños(self, años):
        self.años = años

    def getPuertas(self):
        return self.puertas
    def setPuertas(self, puertas):
        self.puertas = puertas

    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo

    def getRuedas(self):
        return self.ruedas
    def setRuedas(self, ruedas):
        self.ruedas = ruedas

    def getTuneado(self):
        return self.tuneado
    def setTuneado(self, tuneado):
        self.tuneado = tuneado

    def salutacio(self):
        print("La marca es: " + self.marca)
        print("Tengo " + self.años + " años")
        print("Tengo " + self.puertas + " puertas")
        print("Mi tipo es: " + self.tipo)
        print("Tengo " + self.ruedas + " ruedas")
        print("Estoy tuneado: " + self.tuneado)
