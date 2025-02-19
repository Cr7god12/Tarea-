from Punto import Punto

class Linea:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Línea formada por los puntos {self.p1} y {self.p2}"

    def dibuja_linea(self):
        print(f"Dibujando línea desde {self.p1} hasta {self.p2}")
