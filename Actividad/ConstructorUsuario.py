from Constructor import *
class ConstructorUsuario(Constructor):
    """Clase heredada de 'Constructor' cuyo objetivo es almacenar y obtener usuarios de la base de datos."""
    def __init__(self,db):
        """:param db una instancia de la clase 'DB'"""
        super().__init__(db)

    def obtenerDatos(self,datoPersistible):
        """
        Método utilizado para obtener la información de un usuario de la base de datos.
        :param datoPersistible: Una instancia de la clase 'usuario' cuyos datos intentarán ser actualizados desde la base de datos.
        :returns la misma instancia de la clase 'usuario' pasada como parámetro con la información actualizada si no ocurrieron erronres.
        :returns None si las credenciales no fueron encontradas en la base de datos.
        """
        CONSULTA = """SELECT * FROM {tablaUsuarios} WHERE {nombreKey} = '{0}' AND {contraseniaKey} = '{1}'""".format(datoPersistible.getNombre().lower(),datoPersistible.getContrasenia(),tablaUsuarios=keys.TABLA_USUARIOS,nombreKey=keys.NOMBRE_USUARIO,contraseniaKey = keys.CONTRASENIA_USUARIO)
        cursor = self.db.connection.cursor()
        cursor.execute(CONSULTA)

        if cursor.rowcount == 0:
            return None
        else:
            datos = cursor.fetchall()
            if len(datos) == 0:
                return None
            datos = datos[0]
            datoPersistible.setNombre(datoPersistible.getNombre().title())
            datoPersistible.setEdad(datos[2])
            datoPersistible.setId(datos[0])

            return datoPersistible

    def insertarDato(self,datoPersistible):
        """Método utilizado para insertar un nuevo usuario dentro de la base de datos en caso de no existir.
        :returns False si no fue posible insertar al usuario, normalmente porque ya existía.
        :returns True si fue posible insertar al usuario en la base de datos."""
        cursor = self.db.connection.cursor()
        CONSULTA = """SELECT {columnaNombreUsuario} FROM {tablaUsuario} WHERE {columnaNombreUsuario} = '{nombreUsuario}' AND {columnaEdad} = '{edadUsuario}'""".format(
            columnaNombreUsuario=keys.NOMBRE_USUARIO,tablaUsuario=keys.TABLA_USUARIOS,nombreUsuario=datoPersistible.getNombre().lower(),
            columnaEdad=keys.EDAD_USUARIO,edadUsuario=datoPersistible.getEdad()
        )

        cursor.execute(CONSULTA)
        if len(cursor.fetchall()) != 0:
            return False

        CONSULTA = """INSERT INTO {tablaUsuarios}({nombreUsuario},{edadUsuario},{contraseniaUsuario})
        VALUES('{nombre}','{edad}','{contrasenia}')""".format(tablaUsuarios = keys.TABLA_USUARIOS,
                                                        nombreUsuario = keys.NOMBRE_USUARIO,
                                                        edadUsuario = keys.EDAD_USUARIO,
                                                        contraseniaUsuario = keys.CONTRASENIA_USUARIO,
                                                        nombre = datoPersistible.getNombre().lower(),
                                                        edad = datoPersistible.getEdad(),
                                                        contrasenia = datoPersistible.getContrasenia())

        cursor.execute(CONSULTA)
        self.db.connection.commit()
        datoPersistible.setId(cursor.lastrowid)
        return True
