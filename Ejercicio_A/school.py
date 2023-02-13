class school:
    def __init__(self, pisos, aulas, mesas, tipo, patios, telefono):
        self.pisos = pisos
        self.aulas = aulas
        self.mesas = mesas
        self.tipo = tipo
        self.patios = patios
        self.telefono = telefono

    def getPisos(self):
        return self.pisos
    def setPisos(self, pisos):
        self.pisos = pisos

    def getAulas(self):
        return self.aulas
    def setAulas(self, aulas):
        self.aulas = aulas

    def getMesas(self):
        return self.mesas
    def setMesas(self, mesas):
        self.mesas = mesas

    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo

    def getPatios(self):
        return self.patios
    def setPatios(self, patios):
        self.patios = patios

    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono = telefono

    def salutacio(self):
        print("El colegio tiene: " + self.pisos + " pisos")
        print("El colegio tiene: " + self.aulas + " aulas")
        print("El colegio tiene: " + self.mesas + " mesas")
        print("Mi tipo es: " + self.tipo)
        print("El colegio tiene: " + self.patios + " patios")
        print("El teléfono del colegio es: " + self.telefono)
