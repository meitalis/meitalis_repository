import math

class Circle():
    def __init__(self,a,p = math.pi):
        self._a = a
        self._p = p

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, p):
        self._p = p

    def area(self):
        return round(self._p * math.pow(self.a,2),2)

    def perim(self):
        return round(2 * self._p * self.a,2)

    def scale(self,factor):
        self.a  += factor

    def __str__(self):
        return f"Circle area {self.area()} perim {self.perim()}"

class Square(Circle):
    def __init__(self, a):
        super().__init__(a,1)

    def perim(self):
        return super().perim() * 2

    def __str__(self):
        return f"Square area {self.area()} perim {self.perim()}"


s = Square(4)
print(s)

c = Circle(4)
print(c)

s.scale(2)
print(s)








