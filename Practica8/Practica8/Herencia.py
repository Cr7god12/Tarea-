class A:
    def __init__(self, x: int, z: int):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class B:
    def __init__(self, y: int, z: int):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class D(A, B):
    def __init__(self, x: int, y: int, z: int):
        A.__init__(self, x, z)
        B.__init__(self, y, z)

    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1

d = D(x=1, y=2, z=3)
print(f"x: {d.x}, y: {d.y}, z: {d.z}")
d.incrementaXZ()     
d.incrementaYZ()     
d.incrementaZ()      
d.incrementaXYZ()    
print(f"x: {d.x}, y: {d.y}, z: {d.z}")
