class Deportista:
    def __init__(self, años):
        self._deporte = "Futbol"
        self._añosPracticando = años

    def setDeporte(self, n):
        self._deporte = n

    def getDeporte(self):
        return self._deporte

    def setAñosPracticando(self, n):
        self._añosPracticando = n

    def getAñosPracticando(self):
        return self._añosPracticando
