from Punto import Punto
from Linea import Linea
from Circulo import Circulo

if __name__ == "__main__":
    
    p1 = Punto(1, 2)
    p2 = Punto(4, 6)

   
    linea = Linea(p1, p2)
    print(linea)
    linea.dibuja_linea()

    circulo = Circulo(p1, 5)
    print(circulo)
    circulo.dibuja_circulo()
