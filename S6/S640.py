#===============================================================================
# class C(object):
#     def f(self):
#         self.x = 1
# 
#     def g(self):
#         self.y = 1
# 
# class A(C):
#     def f(self):
#         self.x = 2
# 
# c = C()
# a = A()
# print(c.f(), ", ", c.g(), ", ", a.f(), ", ",a.g())
# print(A.__bases__)
#===============================================================================


class E:
    y = 'E'

class F:
    x = 'F'

class B(E, F):
    pass

class C(F):
    pass

class D(F):
    x = 'D'
    y = 'D'

class A(B, C, D):
    pass

print(A.mro())
