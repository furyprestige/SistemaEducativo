from ConstructorUsuario import *
class ConstructorPuntaje(Constructor):
    """Clase heredada de 'Constructor' cuyo objetivo es almacenar y obtener los puntajes de las distintas materias
    desde la base de datos."""

    def __init__(self,db):
        """:param db: una instancia de la clase 'DB'"""
        super().__init__(db)

    def obtenerDatos(self,datoPersistible:Usuario,esConsulta=False):
        """
        Modifica o únicamente devuelve los puntajes del usuario desde la base de datos.
        :param datoPersistible: El usuario del que se obtendrán los puntajes.
        :param esConsulta: si se establece en 'True', automáticamente se modificarán los puntajes del usuario por los que
        se obtengan de la base de datos. Si se establece en 'False' (valor por defecto) sólo se retornarán en la siguiente forma: ('id:int','materia:str','puntaje:str','id del usuario:int').
        :return: se retornan los puntajes en la forma: ('id:int','materia:str','puntaje:str','id del usuario:int') si el parametro de 'esConsulta' se envía como False (valor por defecto).
        None si no hay puntajes existentes para el usuario.
        """
        CONSULTA = """SELECT * FROM {tablaPuntajes} WHERE {id_usuario_columna} = '{id_usuario}'""".format(
            tablaPuntajes=keys.TABLA_PUNTAJES,id_usuario_columna=keys.ID_USUARIO_MATERIAS,id_usuario=datoPersistible.getId()
        )
        cursor = self.db.connection.cursor()
        cursor.execute(CONSULTA)

        datos = cursor.fetchall()

        if(len(datos) == 0):
            return None
        elif not esConsulta:
            for row in datos:
                datoPersistible.addPuntaje(int(row[2]),row[1])
        return datos



    def insertarDato(self,datoPersistible:Usuario):
        """Inserta un nuevo puntaje en la base de datos.
        El puntaje que se agregará será el que esté conectado a la materia que devuelva el método 'getMateriaEntrenada()' del usuario.
        Su etiqueta será la materia propia.
        En caso de que ya exista un puntaje previo para la materia en la base de datos, se actualiza. De lo contrario, se inserta un nuevo registro.
        :param datoPersistible el usuario al que pertenece el puntaje a agregar.
        """
        datos = self.obtenerDatos(datoPersistible,esConsulta=True)

        if datos != None:
            CONSULTA = """UPDATE {tabla_puntajes}
            SET {columnaPuntaje} = '{puntaje}'
            WHERE {id_Usuario_columna} = '{id_usuario}' AND {materia_columna} = '{materia}'""".format(
                tabla_puntajes=keys.TABLA_PUNTAJES,columnaPuntaje = keys.PUNTAJE,
                puntaje=datoPersistible.getPuntajes()[datoPersistible.getMateriaEntrenada()],
                id_Usuario_columna=keys.ID_USUARIO_MATERIAS,
                id_usuario=datoPersistible.getId(),materia_columna=keys.MATERIA,
                materia=datoPersistible.getMateriaEntrenada()
            )
            cursor = self.db.connection.cursor()
            cursor.execute(CONSULTA)
            self.db.connection.commit()
            return

        CONSULTA = """INSERT INTO {tablaPuntajes}({materiaColumna},{puntajeColumna},{idUsuarioColumna})
        VALUES ('{materia}','{puntaje}','{idUsuario}')""".format(tablaPuntajes = keys.TABLA_PUNTAJES,
                                                                 materia = datoPersistible.getMateriaEntrenada(),
                                                                 puntaje=datoPersistible.getPuntajes()[datoPersistible.getMateriaEntrenada()],
                                                                 idUsuario=datoPersistible.getId(),
                                                                 materiaColumna=keys.MATERIA,
                                                                 puntajeColumna=keys.PUNTAJE,
                                                                 idUsuarioColumna=keys.ID_USUARIO_MATERIAS
                                                                 )
        cursor = self.db.connection.cursor()
        cursor.execute(CONSULTA)
        self.db.connection.commit()