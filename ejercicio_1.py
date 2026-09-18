class Edades:
    @staticmethod
    def calcular_edalber(edjuan):
        return 2 * edjuan / 3

    @staticmethod
    def calcular_edana(edjuan):
        return 4 * edjuan / 3

    @staticmethod
    def calcular_edmama(edjuan, edalber, edana):
        return edjuan + edalber + edana


def main():
    print("Ingrese la edad de Juan")
    edjuan = float(input())

    edalber = Edades.calcular_edalber(edjuan)
    edana = Edades.calcular_edana(edjuan)
    edmama = Edades.calcular_edmama(edjuan, edalber, edana)

    print(f"Edad de Alberto: {edalber}")
    print(f"Edad de Ana: {edana}")
    print(f"Edad de Juan: {edjuan}")
    print(f"Edad de la Mama: {edmama}")


if __name__ == "__main__":
    main()