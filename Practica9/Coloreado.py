import random
import math
from abc import ABC, abstractmethod

class Coloreado(ABC):
    @abstractmethod
    def como_colorear(self):
        pass

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio * self.radio

    def perimetro(self):
        return 2 * math.pi * self.radio

figuras = []
for _ in range(5):
    tipo = random.choice([1, 2])
    color = random.choice(['Rojo', 'Azul', 'Verde', 'Amarillo'])
    
    if tipo == 1:
        lado = random.uniform(1, 10)  
        figuras.append(Cuadrado(lado, color))
    else:
        radio = random.uniform(1, 10)  
        figuras.append(Circulo(radio, color))

for figura in figuras:

    if isinstance(figura, Cuadrado):
        tipo_figura = "Cuadrado"
    elif isinstance(figura, Circulo):
        tipo_figura = "Círculo"
    
    print(f"Figura: {tipo_figura}")
    print(figura)  
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}")
    
    if isinstance(figura, Coloreado):
        print(figura.como_colorear())
    
    print()
