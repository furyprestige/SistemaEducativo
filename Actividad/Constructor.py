from abc import ABC,abstractmethod

import DB
import DatoPersistible
from ConstantesBaseDatos import ConstantesBaseDatos as keys
from Usuario import Usuario

class Constructor(ABC):
    """Clase abstracta encargada de definir los métodos y el constructor que todas las clases concretas deben tener y
    cuyo objetivo sea insertar y obtener información de la base de datos."""
    def __init__(self,db:DB.DB):
        self.db = db

    @abstractmethod
    def obtenerDatos(self,datoPersistible:DatoPersistible.DatoPersistible,esConsulta=False):
        pass

    @abstractmethod
    def insertarDato(self,datoPersistible:DatoPersistible.DatoPersistible):
        pass