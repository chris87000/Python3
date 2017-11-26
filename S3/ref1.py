
s = [1,2,3,4]
t = [3,4,5,6]
     
for inc, (i,j) in enumerate(zip(s,t)):
    print(inc, ', ',i,j)