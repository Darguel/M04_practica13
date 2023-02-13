class university:
    def __int__(self, aulas, direccion, pisos, provincia, numAlum, numProf):
        self.aulas = aulas
        self.direccion = direccion
        self.pisos = pisos
        self.provincia = provincia
        self.numAlum = numAlum
        self.numProf = numProf

    def getAulas(self):
        return self.aulas

    def setAulas(self, aulas):
        self.aulas = aulas

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getPisos(self):
        return self.pisos

    def setPisos(self, pisos):
        self.pisos = pisos

    def getProvincia(self):
        return self.provincia

    def setProvincia(self, provincia):
        self.provincia = provincia

    def getNumAlum(self):
        return self.numAlum

    def setNumAlum(self, numAlum):
        self.numAlum = numAlum

    def getNumProf(self):
        return self.numProf

    def setNumProf(self, numProf):
        self.numProf = numProf

    def info(self):
        print("los datos de la univercidad son: \n numero de aulas" + self.aulas)
        print("Direccion: " + self.direccion)
        print("Numero de pisos : " + self.pisos)
        print("Provincia: " + self.provincia)
        print("Numero de alumnos: " + self.numAlum)
        print("Numero se profesores: " + self.numProf)
