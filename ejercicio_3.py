class Nomina:
    @staticmethod
    #se calcula el salario bruto
    def calcular_salario_bruto(horas_trabajadas, valor_hora):
        return horas_trabajadas * valor_hora

    @staticmethod
    #se calcula el valor de la retención en la fuente
    def calcular_valor_retefuente(porcentaje_retefuente, salario_bruto):
        return porcentaje_retefuente * salario_bruto

    @staticmethod
    #se calcula el salario neto
    def calcular_salario_neto(salario_bruto, valor_retefuente):
        return salario_bruto - valor_retefuente


# variables
horas_trabajadas = 48.0
valor_hora = 5000.0
retencion = 12.5
porcentaje_retefuente = retencion / 100

# calculos
salario_bruto = Nomina.calcular_salario_bruto(horas_trabajadas, valor_hora)
valor_retefuente = Nomina.calcular_valor_retefuente(porcentaje_retefuente, salario_bruto)
salario_neto = Nomina.calcular_salario_neto(salario_bruto, valor_retefuente)

# Impresión de resultados
print("salario bruto:", salario_bruto)
print("retencion en la fuente:", valor_retefuente)
print("salario neto:", salario_neto)