from Punto import Punto

class Circulo:
    def __init__(self, centro: Punto, radio: float):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Círculo con centro en {self.centro} y radio {self.radio}"

    def dibuja_circulo(self):
        print(f"Dibujando círculo con centro en {self.centro} y radio {self.radio}")
