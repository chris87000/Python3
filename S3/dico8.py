s = set()
print(type(s))
     
s = {1,2,3,'a',True}

a = [1,2,3,1,18,30,4,1]

be =set(a)
print(be, ", ", len(be))

if 1 in be:
    print("OK")
 
s.add('alice')

print(s)

# add only elements which don't appear in the original set
s.update([1,2,3,4,5,6,6])
print(s)

s1={1,2,3}
s2 = {3,4,5}
print(s1-s2)
print(s1|s2)     
print(s1 & s2)

print("**"*10)
a=[0]
s = set(a)
print(s)