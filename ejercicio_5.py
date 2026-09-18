pi=3.1415
class Calculos:
    pi=3.1415
    @staticmethod
    def calcular_longitud_circunferencia(radio):
        # Usamos math.pi para obtener el valor de PI
        return 2 * pi * radio

    @staticmethod
    def calcular_area_circulo(radio):
        
        return pi * (radio ** 2)

# Se solicita el valor del radio
radio = float(input("Ingrese el radio del círculo: "))

# metodos
longitud_circunferencia = Calculos.calcular_longitud_circunferencia(radio)
area_circulo = Calculos.calcular_area_circulo(radio)

# Imprimimos los resultados
print("Longitud circunferencia: ", longitud_circunferencia)
print("Área círculo: ", area_circulo)