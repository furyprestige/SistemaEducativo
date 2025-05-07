import ConstantesBaseDatos
import DB
import Usuario
from ConstructorPuntaje import ConstructorPuntaje as constructor
from EntrenadorMatematicas import EntrenadorMatematicas
import os

class Home:
    """Clase que tiene acceso a todos los entrenadores.
    Se recomienda usar el patrón de la fábrica al agregar más entrenadores."""
    _usuario = None
    _constructorPuntaje = constructor(DB.DB(ConstantesBaseDatos.ConstantesBaseDatos.PATH_DB))

    @classmethod
    def start(cls,usuario:Usuario.Usuario):
        Home._usuario = usuario
        Home._obtenerPuntajes()
        while True:
            os.system('cls') #Se limpia la pantalla.

            print("¡Bienvenido(a) {0}!".format(usuario.getNombre()))
            print("Tus puntajes: {0}".format(Home._usuario.getPuntajes()))

            entrenador = EntrenadorMatematicas()

            entrenador.start()

            #Esto se ejecuta una vez que el entrenamiento ha finalizado.
            Home._usuario.addPuntaje(entrenador.getPuntaje(),entrenador.getMateria())
            Home._usuario.setMateriaEntrenada(entrenador.getMateria())
            Home._usuario.setUltimoPuntaje(entrenador.getPuntaje())
            Home._constructorPuntaje.insertarDato(Home._usuario) #Se agrega el puntaje obtenido a la base de datos.


    @classmethod
    def _obtenerPuntajes(cls):
        Home._constructorPuntaje.obtenerDatos(Home._usuario) #Se actualizan todos los puntajes del usuario desde la base de datos.