# x = 1
# def f():
#     print(x)
#     x = 2
# print(f())
# 
# a = "a dans module"
# b = "b dans module"

class C:
    a = "a dans C"
    b = "b dans C"

    def f(self):
        b = "b dans f"

        def g():
            print(a)
            print(b)
        g()
C().f()