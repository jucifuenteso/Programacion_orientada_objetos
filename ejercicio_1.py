class Edades:


    #Se calcula la edad de alberto
    @staticmethod
    def calcular_edadalberto(edadjuan):
        return 2 * edadjuan / 3

    @staticmethod
    def calcular_edadana(edadjuan):
        return 4 * edadjuan / 3

    @staticmethod
    def calcular_edadmama(edadjuan, edadalberto, edadana):
        return edadjuan + edadalberto + edadana


def main():
    print("Ingrese la edad de Juan")
    edadjuan = float(input())

    edadalberto = Edades.calcular_edadalberto(edadjuan)
    edadana = Edades.calcular_edadana(edadjuan)
    edadmama = Edades.calcular_edadmama(edadjuan, edadalberto, edadana)

    print(f"Edad de Alberto: {edadalberto}")
    print(f"Edad de Ana: {edadana}")
    print(f"Edad de Juan: {edadjuan}")
    print(f"Edad de la Mama: {edadmama}")


if __name__ == "__main__":
    main()