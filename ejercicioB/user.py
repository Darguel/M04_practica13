class user:
    def __int__(self, pelo, edad, telefono, direccion, nom, apell):
        self.pelo = pelo
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.nom = nom
        self.apell = apell

    def getPelo(self):
        return self.pelo

    def setPelo(self, pelo):
        self.pelo = pelo

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion

    def geNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getApell(self):
        return self.apell

    def setApell(self, apell):
        self.apell = apell

    def salutacio(self):
        print("Los datos del user son: \n colo de pelo" + self.pelo)
        print("edad: " + self.edad)
        print("Numero de telefono : " + self.telefono)
        print("direccion: " + self.direccion)
        print("nombre: " + self.nom)
        print("apellidos: " + self.apell)