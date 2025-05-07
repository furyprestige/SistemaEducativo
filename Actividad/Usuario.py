from DatoPersistible import DatoPersistible


class Usuario(DatoPersistible):
    """Clase que representa a un usuario. Hereda de dato persistible."""
    def __init__(self, nombre, edad,contrasenia):
        self._nombre = nombre
        self._edad = edad
        self._puntajes = {}
        self._contrasenia = contrasenia
        self._materiaEntrenada = None
        self._ultimoPuntaje = None

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self,edad):
        self._edad = edad

    def setMateriaEntrenada(self,materia):
        """Debe llamarse cada que se realice un entrenamiento.
        :param materia: la materia que acaba de ser entrenada."""
        self._materiaEntrenada = materia

    def setUltimoPuntaje(self,puntaje):
        """Debe llamarse cada que se realice un entrenamiento.
        :param puntaje: el puntaje obtenido en el último entrenamiento."""
        self._ultimoPuntaje = puntaje

    def setContrasenia(self,contrasenia):
        self._contrasenia = contrasenia

    def getMateriaEntrenada(self):
        """:returns la última materia que fue entrenada en la sesión actual."""
        return self._materiaEntrenada

    def getUltimoPuntaje(self):
        """:returns el último puntaje obtenido en el entrenamiento más reciente de la sesión actual."""
        return self._ultimoPuntaje

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getContrasenia(self):
        return self._contrasenia

    def getPuntajes(self):
        """:returns el hashtable de puntajes."""
        return self._puntajes

    def addPuntaje(self,puntaje,materia):
        """Actualiza el hashtable de puntajes.
        :param materia: materia a la que se desea agregar un puntaje.
        :param puntaje el puntaje que desea agregarse bajo la key 'materia'"""
        if materia in self._puntajes:
            self._puntajes[materia] = self._puntajes[materia]+puntaje
        else:
            self._puntajes[materia] = puntaje

    def remplazarPuntaje(self,puntaje,materia):
        """Sobrescribe el puntaje bajo la key 'materia' del hashtable de puntajes."""
        self.puntajes[materia] = puntaje

    def reemplazarPuntajes(self,puntajes:dict):
        """Sobrescribe el hashtable de puntajes."""
        self._puntajes = puntajes

    def __str__(self):
        return self.nombre+" "+str(self.edad)
