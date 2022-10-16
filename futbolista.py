from deportista import Deportista
from persona import Persona


class Futbolista(Persona, Deportista):

    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sex, años, goles, rojas, pierna):
        Persona.__init__(nombre, edad, altura, sex)
        Deportista.__init__(años)
        self._golesMarcados = goles
        self._tarjetasRojas = rojas
        self._piernaHabil = pierna
        Futbolista.listaFutbolistas.append(self)

    def setGolesMarcados(self, n):
        self.__golesMarcados = n

    def getGolesMarcados(self):
        return self.__golesMarcados

    def setTarjetasRojas(self, n):
        self._tarjetasRojas = n

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setPiernaHabil(self, n):
        self._piernaHabil = n

    def getPiernaHabil(self):
        return self._piernaHabil

    def setListaFutbolistas(self, n):
        self.listaFutbolistas = n

    def getListaFutbolistas(self):
        return self.listaFutbolistas

    def __str__(self):

        string = "Mi nombre es {persona} soy profesional en el deporte {deporte} Tengo {edad} años de edad y llevo {anos} años en el deporte"
        string.format(
            nombre=self.getNombre,
            deporte=self.getDeporte,
            edad=self.getNombre,
            anos=self.getAñosPracticando,
        )
        return string
