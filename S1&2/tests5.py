import re
from time import clock as now
import cProfile

def test(f, *args, **kargs):
    start = now()
    f(*args, **kargs)
    print ("The function %s lasted: %f" %(f.__name__, now() - start))
    
# coding: utf-8
print("\n")
print("*"*100)
pattern = re.compile(r'\w+\s[\d-]+\s[\d:,]+\s(.*(?<!authentication\s)failed)')
ze = pattern.findall("INFO 2013-09-17 12:13:44,487 authentication failed")
print(ze)
az= pattern.findall("INFO 2013-09-17 12:13:44,487 something else failed")
print(az)

print("\n")
print("*"*100)
def alternation(text):
    pat = re.compile('spa(in|niard)')
    pat.search(text)
test(alternation, "spain")

print("\n")
print("*"*100)
cProfile.run("alternation('spaniard')")