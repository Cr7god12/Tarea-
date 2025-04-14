class A:
    def saludar(self):
        print("Hola desde A")

class B(A):
    def saludar(self):
        print("Hola desde B")

class C(A):
    def saludar(self):
        print("Hola desde C")

class D(B, C):
    def saludar(self):
        print("Hola desde D")
        A.saludar(self)
        B.saludar(self)
        C.saludar(self)

d = D()
d.saludar()
