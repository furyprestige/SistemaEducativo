# Sistema de Entrenamiento y Persistencia de Usuarios
Este proyecto en Python implementa un sistema de manejo de usuarios y puntajes en SQLite, con clases abstractas para la persistencia (`Constructor`, `DatoPersistible`) y entrenadores de materias (por defecto, Matemáticas). Incluye:
- **ConstantesBaseDatos**: rutas, nombres de tablas y columnas.
- **DB**: conexión y creación de tablas SQLite.
- **ConstructorUsuario** y **ConstructorPuntaje**: CRUD de usuarios y puntajes.
- **EntrenadorMatematicas**: generación de preguntas y cálculo de puntaje.
- **Home** y **SesionScreen**: flujo de inicio de sesión y navegación.

## Requisitos técnicos
- **Python 3.12**  
- Módulo **sqlite3** (incluido en la librería estándar)  
- Ejecutable en Windows (usa `msvcrt` para pausa) o adaptar `os.system('cls')` a `clear` en Unix  
- IDE o editor de texto (VSCode, PyCharm, etc.)

## Objetivo de la actividad
1. Modelar persistencia con SQLite y clases abstractas.  
2. Diseñar un patrón constructor para operaciones de base de datos.  
3. Implementar un entrenador de preguntas interactivas.  
4. Gestionar flujo de usuario: inicio de sesión, creación de cuenta y registro de puntajes.

## Ejecutar la Solución
- Ejecuta el código `python main.py`
- Aparecerá el menú de inicio de sesión o creación de cuenta.
- Tras iniciar sesión, accederás al menú principal con el entrenador de Matemáticas.
- Al terminar cada sesión de entrenamiento, el puntaje se guardará automáticamente en la base de datos Usuarios.db.

## Uso y Personalización
- Agregar nuevos entrenadores: crear clase que herede de Entrenador y registrar en Home.py.
- Interfaz de consola: reemplazar os.system('cls') por clear para Unix, o integrar una librería CLI más avanzada.
