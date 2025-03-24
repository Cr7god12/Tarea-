from multimethod import multimethod
import math
class FigurasGeometricas:
    # Círculo
    @multimethod
    def area(self, radio: float):
        return math.pi * radio * radio
    # Rectángulo
    @multimethod
    def area(self, base: float, altura: float):
        return base * altura
    # Triángulo rectángulo
    @multimethod
    def area(self, base: int, altura: int):
        return 0.5 * base * altura
    # Trapecio
    @multimethod
    def area(self, baseMayor: float, baseMenor: float, altura1: float):
        return ((baseMayor + baseMenor) * altura1) / 2
    # Pentágono regular
    @multimethod
    def area(self, lado: int, apotema: float):
        return (5 * lado * apotema) / 2

fig = FigurasGeometricas()
print("Área del círculo:", fig.area(5))
print("Área del rectángulo:", fig.area(4.0, 6.0))
print("Área del triángulo rectángulo:", fig.area(3, 4))
print("Área del trapecio:", fig.area(6.0, 4.0, 5.0))
print("Área del pentágono:", fig.area(4, 5.0))
