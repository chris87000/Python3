heteroclite = {'marc', 12, 'pierre', (1, 2, 3), 'pierre'}
print(heteroclite, ", ", type(heteroclite))

heteroclite2 = set(['marc', 12, 'pierre', (1, 2, 3), 'pierre'])
print(heteroclite2)

print("**"*10)
ensemble_vide = set()
print(type(ensemble_vide))

print("**"*10)
autre_ensemble_vide = set([])
print(type(autre_ensemble_vide))

print("**"*10)
print(type({}))
print(set())
print(set([]))

s = set()
s = {1,2,3,6,7,9,586,47,64,98}
p = set()
p = {11,99,66}

s.add(p)
print(s)

f = frozenset()
f = {333,555,999}
s.add(f)
print(s)      