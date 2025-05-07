from abc import ABC, abstractmethod

class Entrenador(ABC):
    """Clase abstracta de la que todos los entrenadores de materias deben heredar.
    Define los métodos abstractos que deben ser implementados."""
    def __init__(self,materia):
        """:param materia es la materia en la que se enfocará el entrenador."""
        self.materia = materia
        self.puntaje = 0

    @abstractmethod
    def generarPreguntas(self):
        """Método abstracto que lanza preguntas al usuario, evalúa las respuestas y acumula puntajes."""
        pass

    @abstractmethod
    def start(self):
        """Método abstracto principal para inicializar el entrenador."""
        pass

    def getPuntaje(self):
        """:returns el puntaje del entrenador."""
        return self.puntaje

    def getMateria(self):
        """:returns la materia vinculada al entrenador."""
        return self.materia