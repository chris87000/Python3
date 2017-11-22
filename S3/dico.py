a = [('ana', 35), ('eve', 30), ('bob', 38)]
age = dict(a)
print(age) 

print("**"*20)

print(age['bob'])
age['bob'] =45 
print(age) 

del age['bob']
print(age) 

print("**"*20)
print(len(age))
print('ana' in age) ; print('bob' in age) 
print("**"*20)


print(age.keys())
print(age.values())
print(age.items() )

print("**"*20)
age['bob']=25
print(age.keys())

for k,v in age.items():
    print(f"{k} {v}")

for k in age:
    print(k)



