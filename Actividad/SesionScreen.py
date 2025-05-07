import ConstantesBaseDatos
import DB
from ConstructorUsuario import ConstructorUsuario as constructor
from Home import Home
from Usuario import Usuario
import os

class SesionScreen:
    """
    Clase utilizada para controlar el inicio de sesión y la creación de cuenta.
    """
    _constructorUsuario = constructor(DB.DB(ConstantesBaseDatos.ConstantesBaseDatos.PATH_DB))
    _usuario = None

    @classmethod
    def start(cls):
        """
        Método de clase principal. Al ejecutarlo, se espera un inicio de sesión o creación de cuenta exitoso.
        Cuando esto ocurre, el usuario es dirigido automáticamente a la ventana principal (Home).
        """
        while SesionScreen._usuario == None:
            print("1.- Iniciar sesion.")
            print("2.- Crear cuenta.")
            opc = input("Selecciona una opción: ")
            while not opc in ("1","2"):
                print("Esa opción es inválida.")
                opc = input("Selecciona una opción: ")
            if opc == "1":
                SesionScreen.iniciarSesion()
            else:
                SesionScreen.crearCuenta()

        Home.start(SesionScreen._usuario)


    @classmethod
    def iniciarSesion(cls):
        """Método de clase que intenta iniciar la sesión de un usuario solicitando sus credenciales.
        Cuando es exitoso, guarda una instancia del usuario en la variable de clase privada '_usuario'"""
        nombre = input("Ingresa tu nombre: ")
        contrasenia = input("Ingresa tu contraseña: ")
        usuario = Usuario(nombre=nombre,contrasenia=contrasenia,edad=-1)
        SesionScreen._usuario = SesionScreen._constructorUsuario.obtenerDatos(usuario)

        if SesionScreen._usuario is None:
            print("El usuario o la contraseña son incorrectos.")
        else:
            return



    @classmethod
    def crearCuenta(cls):
        """Método de clase que intenta crear la cuenta para un usuario solicitando sus credenciales.
        Cuando es exitoso, guarda una instancia del usuario en la variable de clase privada '_usuario'"""
        regresar = input("Ingresa 0 para regresar u otro valor para continuar: ")
        if regresar == "0":
            return

        nombre = input("Ingresa tu nombre: ")
        edad = input("Ingresa tu edad: ")
        contrasenia = input("Ingresa tu contraseña: ")

        usuarioNuevo = Usuario(nombre,edad,contrasenia)

        if not SesionScreen._constructorUsuario.insertarDato(usuarioNuevo):
            print("El usuario que intentas registrar ya existe.")
        else:
            SesionScreen._usuario = usuarioNuevo
            print("Cuenta creada exitosamente.")
