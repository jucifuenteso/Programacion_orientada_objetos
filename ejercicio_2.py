# se define la clase
class Calculo:
    def __init__(self, x, y):  # constructor
        self.suma = 0  
        self.x = x   
        self.y = y     
        print(f"SUMA: {self.suma}, X: {self.x}, Y: {self.y}")

    def sumar_x_inicial(self): 
        # SUMA = SUMA + X
        self.suma = self.suma + self.x
        print(f"SUMA: {self.suma}, X: {self.x}, Y: {self.y}")

    def actualizar_x(self):  
        # X = X + Y ** 2
        self.x = self.x + (self.y ** 2)
        print(f"SUMA: {self.suma}, X: {self.x}, Y: {self.y}")

    def actualizar_suma_final(self):
        # SUMA = SUMA + X / Y
        self.suma = self.suma + (self.x / self.y)
        print(f"SUMA: {self.suma}, X: {self.x}, Y: {self.y}")




#Objecto
calculo1 = Calculo(x=20, y=40)

# usamos objetos
calculo1.sumar_x_inicial()
calculo1.actualizar_x()
calculo1.actualizar_suma_final()
