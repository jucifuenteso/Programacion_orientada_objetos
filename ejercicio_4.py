import math


class Calculos:
    @staticmethod
    def calcular_cuadrado(numero):
        return math.pow(numero, 2)

    @staticmethod
    def calcular_cubo(numero):
        return math.pow(numero, 3)



numero = 4.0

# Llamada a los métodos estáticos de la clase Calculos
cuadrado = Calculos.calcular_cuadrado(numero)
cubo = Calculos.calcular_cubo(numero)

print("Cuadrado:" , cuadrado)
print("Cubo:" , cubo)