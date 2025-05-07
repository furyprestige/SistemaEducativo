import random
import msvcrt
from Entrenador import Entrenador
import os
class EntrenadorMatematicas(Entrenador):
    """Entrenador concreto que ayuda al estudiante a mejorar sus habilidades en sumas, restas, multiplicaciones, divisiones y jerarquía de operaciones.
    La complejidad de cada pregunta puede ajustarse en cada sesión de entrenamiento."""
    def __init__(self):
        super().__init__("Matemáticas")
        #Las operaciones y los símbolos tienen la misma posición.
        self.simbolos =["*","/","+","-"]
        self.operaciones = [lambda x,y:x*y, lambda x,y: x/y, lambda x,y: x+y, lambda x,y: x-y]


    def start(self):
        """Método para iniciar al entrenador.
        :returns el puntaje del entrenamiento llevado a cabo."""
        temario = """¿Qué te gustaría practicar?
        1.- Multiplicaciones.
        2.- Divisiones.
        3.- Sumas.
        4.- Restas.
        5.- Jerarquía de operaciones."""

        print(temario)

        opc = "-1"

        while not opc in ("12345"):
            opc = input("Elige una opción: ")

        #Esto NO significa que las respuestas NO tengan decimales.
        decimales = input("""¿Incluir decimales en los valores?
        1.- Sí.
        2.- No.
        Opción: """)
        while decimales not in ("12"):
            decimales = input("""¿Incluir decimales?
                    1.- Sí.
                    2.- No.
                    Opción: """)

        valores = -1
        while valores < 2:
            try:
                #Es la cantidad de valores en cada operación. Por ejemplo: una suma de 5 valores.
                valores = int(input("¿Cuántos valores a operar? El mínimo son 2: "))
            except ValueError:
                pass

        digitos = -1

        while digitos < 1:
            try:
                digitos = int(input("¿Cuántos digitos tendrá cada valor como máximo? Sin incluir decimales: "))
            except ValueError:
                pass

        digitosDecimales = 0
        if decimales == '1':
            while digitosDecimales < 1:
                try:
                    digitosDecimales = int(input("¿Cuántos digitos decimales tendrá cada valor como máximo? El mínimo es 1: "))
                except ValueError:
                    pass

        os.system('cls') #Se limpia la pantalla con esta línea
        print("Tu entrenamiento está por comenzar.")
        print("Para dejar de recibir preguntas, ingresa la letra 'n'\n")
        self.generarPreguntas(decimales,digitos,valores,digitosDecimales,opc)
        print("¡Felicidades por tu entrenamiento! Ganaste: {0} puntos.".format(self.puntaje))
        print("Presione cualquier tecla para continuar...")
        msvcrt.getwch() #Se pausa la ejecución hasta recibir una respuesta del teclado.
        return self.puntaje

    def generarValores(self, digitos, cantidadValores, digitosDecimales):
        """Método que genera todos los valores necesarios para lanzar la pregunta.
        :param digitos es la cantidad de digitos que tendrá cada valor como máximo.
        :param cantidadValores es la cantidad de valores que tendrá la pregunta.
        :param digitosDecimales es la cantidad de digitos decimales que tendrá cada valor como máximo.
        :returns una lista con todos los valores (float) necesarios para lanzar la pregunta."""

        return [random.randint(1, (10 ** digitos)-1) + float("." + str(random.randint(0, (10 ** digitosDecimales)-1))) for i in range(cantidadValores)]


    def generarPreguntas(self,decimales,digitos,cantidadValores,digitosDecimales,operacionEntrenando):
        """Se lanzan preguntas al usuario del tema seleccionado.
        Si la respuesta que da es correcta, se suma un punto en la variable de instancia 'puntaje'."""
        respuestaUsuario = -1

        while respuestaUsuario != 'n':
            respuesta = 'a'
            valores = self.generarValores(digitos,cantidadValores,digitosDecimales)
            operacionEntrenando = int(operacionEntrenando)
            pregunta = ""
            for valor in valores:
                if operacionEntrenando != 5:
                    simbolo = self.simbolos[operacionEntrenando-1]
                else:
                    simbolo = random.choice(self.simbolos)
                pregunta += str(valor) + " " + simbolo + " "
            pregunta = pregunta[:len(pregunta) - 2]
            respuestaCorrecta = eval(pregunta) #eval convierte un texto en una instrucción ejecutable para python.
            print(pregunta)
            respuestaUsuario = None
            while True:
                try:
                    respuestaUsuario = input("¿Cuál es la respuesta? REDONDEA A TRES DECIMALES SI ES POSIBLE: ")
                    if respuestaUsuario == 'n':
                        break
                    else:
                        respuestaUsuario = float(respuestaUsuario)
                    break
                except ValueError:
                    print("Valor incomprensible.")

            respuestaCorrecta = round(respuestaCorrecta,3)

            if respuestaUsuario != 'n' and respuestaUsuario != respuestaCorrecta:
                print("Incorrecto. La respuesta era: {0}".format(respuestaCorrecta))
            elif respuestaUsuario != 'n' and respuestaUsuario == respuestaCorrecta:
                print("¡Correcto! Ganaste 1 punto.")
                self.puntaje += 1