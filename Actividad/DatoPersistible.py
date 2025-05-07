class DatoPersistible:
    """Clase abstracta que deben implementar todas aquellas clases que tengan información persistible en una base de datos."""
    def __init__(self):
        self._id = -1

    def setId(self,id):
        """Establece el id que se tiene dentro de la base de datos."""
        self._id = id

    def getId(self):
        """Se obtiene el id con el que existe en la base de datos."""
        return self._id