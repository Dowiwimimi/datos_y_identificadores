
"""evaluación básica de shinigami (Bleach)
descripción: utiliza distintos tipos de datos para evaluar si un Shinigami puede usar su Bankai"""

# aqui comienza la entrada de datos
nombre_shinigami = input("Ingrese el nombre del Shinigami: ") 
nivel_reiatsu = int(input("Ingrese el nivel de reiatsu: "))  

#valor fijo para el ejemplo
multiplicador_bankai = 1.5 

#evaluación simple
puede_usar_bankai = nivel_reiatsu >= 1500 * multiplicador_bankai  

#esta es la salida de resultados
print("Resultado de la evaluación")
print("Shinigami:", nombre_shinigami)

if puede_usar_bankai:
    print("Estado: Puede usar Bankai.")
else:
    print("Estado: Aún no puede usar Bankai .")