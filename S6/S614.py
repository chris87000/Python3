class C:
    def f(self):
        self.x = 1

    def g(self):
        self.y = 1

class A(C):
    def f(self):
        self.x = 2

c = C()
a = A()
print(c.f(), ", ", c.g(), ", ", a.f(), ", ",a.g())
print(vars(a))