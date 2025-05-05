from multimethod import multimethod

class Ministerio:
    def __init__(self, nombre="", direccion="", nroEmpleados=4):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = nroEmpleados
        self.empleados = [
            ["pedro", "rojas", "luna"],
            ["lucy", "sosa", "rios"],
            ["ana", "perez", "rojas"],
            ["saul", "arce", "calle"]
        ]
        self.edades = [35, 43, 26, 29]
        self.sueldos = [2500.0, 3250.0, 2700.0, 2500.0]

    def __str__(self):
        cad = f"Ministerio: {self.nombre}, Dirección: {self.direccion}, nroEmpleados: {self.nroEmpleados}\n"
        for i in range(self.nroEmpleados):
            cad += f"Nombre: {self.empleados[i][0]} {self.empleados[i][1]}  {self.empleados[i][2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}\n"
        return cad

    def eliminarEmpleado(self, edad):
        for i in range(self.nroEmpleados - 1, -1, -1):
            if self.edades[i] == edad:
                del self.empleados[i]
                del self.edades[i]
                del self.sueldos[i]
                self.nroEmpleados -= 1

    def __add__(self, otros):
        otro, nombre = otros
        if isinstance(otro, Ministerio):
            for i in range(self.nroEmpleados):
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

    def menorEdad(self):
        menor = float('inf')
        for edad in self.edades:
            if edad < menor:
                menor = edad
        return menor if menor != float('inf') else None

    def menorSueldo(self):
        menor = float('inf')
        for sueldo in self.sueldos:
            if sueldo < menor:
                menor = sueldo
        return menor if menor != float('inf') else None

    @multimethod
    def mostrar(self, edad: int):
        for i in range(self.nroEmpleados):
            if self.edades[i] == edad:
                print(f"Nombre: {self.empleados[i][0]} Paterno: {self.empleados[i][1]} Materno: {self.empleados[i][2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")

    @multimethod
    def mostrar(self, sueldo: float):
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == sueldo:
                print(f"Nombre: {self.empleados[i][0]} Paterno: {self.empleados[i][1]} Materno: {self.empleados[i][2]}, Edad: {self.edades[i]}, Sueldo: {self.sueldos[i]}")


if __name__ == "__main__":
    m1 = Ministerio("Ministerio de Salud", "Av. Camacho")
    m2 = Ministerio("Ministerio de Educación", "Av. Arce")
    print("Ministerio 1:")
    print(m1)
    print("Ministerio 2:")
    print(m2)
    print("Eliminando empleado con edad x de Ministerio 1:")
    m1.eliminarEmpleado(26)
    print(m1)
    print("Moviendo 'saul' de Ministerio 1 a Ministerio 2:")
    m2 = m1 + (m2, "saul")
    print("Ministerio 1 después de mover:")
    print(m1)
    print("Ministerio 2 después de recibir:")
    print(m2)
    print("Empleado con menor edad en Ministerio 1:")
    edad_menor = m1.menorEdad()
    m1.mostrar(edad_menor)
    print("Empleado con menor sueldo en Ministerio 1:")
    edad_menor = m1.menorSueldo()
    m1.mostrar(edad_menor)
    print("Empleado con menor edad en Ministerio 2:")
    edad_menor = m2.menorEdad()
    m2.mostrar(edad_menor)
    print("Empleado con menor sueldo en Ministerio 2:")
    edad_menor = m2.menorSueldo()
    m2.mostrar(edad_menor)