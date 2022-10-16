class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo

    def setNombre(self, n):
        self._nombre = n

    def getNombre(self):
        return self._nombre

    def setEdad(self, n):
        self._edad = n

    def getEdad(self):
        return self._edad

    def setAltura(self, n):
        self._altura = n

    def getAltura(self):
        return self._altura

    def setSexo(self, n):
        self._sexo = n

    def getSexo(self):
        return self._sexo
