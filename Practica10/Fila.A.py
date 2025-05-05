from multimethod import multimethod

class LineaTeleferico:
    
    def __init__(self, color="", tramo="", nroCabinas=0, nroEmpleados=4):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = nroEmpleados
        self.empleados = [["pedro", "rojas", "luna"],
                          ["lucy", "sosa", "rios"],
                          ["ana", "perez", "rojas"],
                          ["saul", "arce", "calle"]]
        self.edades = [50, 43, 50, 29]       
        self.sueldos = [2500.0, 3250.0, 2700.0, 3200.0] 

    def __str__(self):
        cad = f"Color: {self.color}, Tramo: {self.tramo}, nroCabinas: {self.nroCabinas}, nroEmpleados: {self.nroEmpleados}\n"
        cad += "Empleados: \n"
        for i in range(len(self.empleados)):
            cad += f"Nombre: {self.empleados[i][0]} {self.empleados[i][1]} {self.empleados[i][2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        return cad

    def eliminarPorApellido(self, apellido):
        for i in range(len(self.empleados) - 1, -1, -1):
            if apellido in self.empleados[i][1:]:
                del self.empleados[i]
                del self.edades[i]
                del self.sueldos[i]
                self.nroEmpleados -= 1

    def __add__(self, otros):
        otro, nombre = otros
        if isinstance(otro, LineaTeleferico):
            for i in range(len(self.empleados)):
                if self.empleados[i][0] == nombre:
                    otro.empleados.append(self.empleados[i])
                    otro.edades.append(self.edades[i])
                    otro.sueldos.append(self.sueldos[i])
                    del self.empleados[i]
                    del self.edades[i]
                    del self.sueldos[i]
                    self.nroEmpleados -= 1
                    otro.nroEmpleados += 1
                    break
        return otro

    def mayorEdad(self):
        mayor = self.edades[0]
        for edad in self.edades:
            if edad > mayor:
                mayor = edad
        return mayor

    def mayorSueldo(self):
        mayor = self.sueldos[0]
        for sueldo in self.sueldos:
            if sueldo > mayor:
                mayor = sueldo
        return mayor

    @multimethod
    def mostrar(self, edad: int):  
        cad = ""
        for i in range(len(self.empleados)):
            if self.edades[i] == edad:
                cad += f"Nombre: {self.empleados[i][0]} {self.empleados[i][1]} {self.empleados[i][2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        print(cad)

    @multimethod
    def mostrar(self, sueldo: float):  
        cad = ""
        for i in range(len(self.empleados)):
            if self.sueldos[i] == sueldo:
                cad += f"Nombre: {self.empleados[i][0]} {self.empleados[i][1]} {self.empleados[i][2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        print(cad)

if __name__ == "__main__":
    t01 = LineaTeleferico("rojo", "Estación Central - Cementerio - 16 de Julio", 20, 4)
    t02 = LineaTeleferico("azul", "Plaza Triangular - San Jorge", 12, 4)

    print("Primer teleférico:")
    print(t01)

    print("Segundo teleférico:")
    print(t02)

    print("Eliminando empleados con apellido 'rojas'")
    t01.eliminarPorApellido("rojas")
    print(t01)

    print("Eliminando empleados con apellido 'arce'")
    t02.eliminarPorApellido("arce")
    print(t02)

    print("Usando operador:")
    t01 + (t02, "saul")
    print("Segundo teleférico después de recibir a 'saul':")
    print(t02)

    print("Mostrar empleados con mayor edad (1er teleférico):")
    edadMayor = t01.mayorEdad()
    t01.mostrar(edadMayor)

    print("Mostrar empleados con mayor sueldo (1er teleférico):")
    sueldoMayor = t01.mayorSueldo()
    t01.mostrar(sueldoMayor)

    print("Mostrar empleados con mayor edad (2do teleférico):")
    edadMayor = t02.mayorEdad()
    t02.mostrar(edadMayor)

    print("Mostrar empleados con mayor sueldo (2do teleférico):")
    sueldoMayor = t02.mayorSueldo()
    t02.mostrar(sueldoMayor)
