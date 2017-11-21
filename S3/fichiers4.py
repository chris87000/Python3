import json

# En partant d'une donnée construite à partir de types de base
data = [
    # des types qui ne posent pas de problème
    [1, 2, 'a', [3.23, 4.32], {'eric': 32, 'jean': 43}],
    # un tuple
    (1, 2, 3),
]

# sauver ceci dans un fichier
with open("s1.json","w", encoding='utf-8') as json_output:
    json.dump(data, json_output)
    
# et relire le résultat 
with open("s1.json", encoding='utf-8') as json_input:
    data2 = json.load(json_input)
    print(data2)

print("première partie de data", data[0] == data2[0])
# par contre le `tuple` se fait encoder comme une `list`
print(f"data[1]:{data[1]}, data2[1]: {data2[1]}")
print("deuxième partie", "entrée", type(data[1]), "sortie", type(data2[1]))