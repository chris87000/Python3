import numpy as np
import matplotlib.pyplot as plt

def pgcd(a, b):
   if a == b:
       return a
   elif b==0:
       return a
   else:
       while a%b != 0 : 
          a, b = b, a%b 
       return b
  
def taxes(income):
    if income <= 11_500:
        return 0
    elif income >11_500 and income <=45_000:
        return int((income-11_500) * (20/100))
    elif income >45_000 and income <=150_000:
        return int((income-28_250) * (40/100))
    elif income > 150_000:
        return int((income-41_777) * (45/100))
    
tt = [0,45000,11500,5000,16500,30000,100000,150000,200000,11504]

for i in tt:
    print(taxes(i))
print("**********"*10)
a = 10
def f():
    global a
    a = a + 10
    b = 20
    def g():
        nonlocal b
        b = b + 20
    g()
    return b

print(f() + a)