import sqlite3
from ConstantesBaseDatos import ConstantesBaseDatos as keys

class DB():
    """Clase que representa una base de datos, hereda de sqlite3."""
    def __init__(self,dbPath):
        """
        Crea una nueva instancia de sqlite3, conecta automáticamente con la base.
        :param dbPath es la ruta de la base de datos. Crea el archivo automáticamente si no existe.
        """
        self.connection = sqlite3.connect(dbPath)
        self.create_tables()

    def create_tables(self):
        """
        Crea las tablas de usuarios y materias si no existen en la base de datos.
        Las propiedades se definen en la clase 'ConstantesBasesDatos'
        """
        consulta = """CREATE TABLE IF NOT EXISTS {0}(
        {idKey} INTEGER PRIMARY KEY AUTOINCREMENT,
        {nombreKey} TEXT,
        {edadKey} TEXT,
        {contrasenia} TEXT);""".format(keys.TABLA_USUARIOS,idKey=keys.ID_USUARIO,nombreKey=keys.NOMBRE_USUARIO,edadKey=keys.EDAD_USUARIO,contrasenia=keys.CONTRASENIA_USUARIO)
        self.connection.execute(consulta)

        consulta = """CREATE TABLE IF NOT EXISTS {0}(
        {idKey} INTEGER PRIMARY KEY AUTOINCREMENT,
        {materiaKey} TEXT,
        {puntajeKey} TEXT,
        {id_usuario_materia} INTEGER,
        FOREIGN KEY({id_usuario_materia}) REFERENCES {tabla_usuarios}({id_usuario}));""".format(keys.TABLA_PUNTAJES,idKey=keys.ID_MATERIA,materiaKey=keys.MATERIA,puntajeKey = keys.PUNTAJE,id_usuario_materia = keys.ID_USUARIO_MATERIAS,tabla_usuarios = keys.TABLA_USUARIOS, id_usuario = keys.ID_USUARIO)

        self.connection.execute(consulta)