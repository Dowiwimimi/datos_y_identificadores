"""evaluación básica de Shinigami - Bleach
Descripción: uso de la poo y distintos tipos de datos para evaluar si un Shinigami puede usar su Bankai"""

#definición de la clase
class Shinigami:

    def __init__(self, nombre_shinigami, nivel_reiatsu):
        #atributos del shinigami
        self.nombre_shinigami = nombre_shinigami
        self.nivel_reiatsu = nivel_reiatsu

    def evaluar_bankai(self):
        #valor fijo para el ejemplo
        multiplicador_bankai = 1.5

        #evaluación simple
        return self.nivel_reiatsu >= 1500 * multiplicador_bankai


#aquí comienza la entrada de datos
nombre_shinigami = input("Ingrese el nombre del Shinigami: ")
nivel_reiatsu = int(input("Ingrese el nivel de reiatsu: "))

#creación del objeto
shinigami = Shinigami(nombre_shinigami, nivel_reiatsu)

# esta es la salida de resultados
print("Resultado de la evaluación")
print("Shinigami:", shinigami.nombre_shinigami)

if shinigami.evaluar_bankai():
    print("Estado: Puede usar Bankai.")
else:
    print("Estado: Aún no puede usar Bankai.")
