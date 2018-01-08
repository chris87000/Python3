class DualQueue:
    """Une double file d'attente FIFO"""

    def __init__(self):
        "constructeur, sans argument"
        self.inputs = []
        self.outputs = []

    def __repr__ (self):
        "affichage"
        return f"<DualQueue, inputs={self.inputs}, outputs={self.outputs}>"

    # la partie qui nous intéresse ici
    def __contains__(self, item):
        "appartenance d'un objet à la queue"
        return item in self.inputs or item in self.outputs
    
    def __len__(self):
        "longueur de la queue"
        return len(self.inputs) + len(self.outputs)        

    # l'interface publique de la classe
    # le plus simple possible et sans aucun contrôle
    def add_input(self, item):
        "faire entrer un objet dans la queue d'entrée"
        self.inputs.insert(0, item)
        
    def move_input_to_output (self):
        "l'objet le plus ancien de la queue d'entrée est promu dans la queue de sortie"
        self.outputs.insert(0, self.inputs.pop())
        
    def emit_output (self):
        "l'objet le plus ancien de la queue de sortie est émis"
        return self.outputs.pop()
   # on construit une instance pour nos essais
queue = DualQueue()
queue.add_input('zero')
queue.add_input('un')
queue.move_input_to_output()
queue.move_input_to_output()
queue.add_input('deux')
queue.add_input('trois')

print(queue)
print(f'len() = {len(queue)}')

print(f"deux appartient-il ? {'deux' in queue}")
print(f"1 appartient-il ? {1 in queue}")

# une première version de DualQueue.__getitem__
# pour uniquement l'accès par index

# on définit une fonction
def dual_queue_getitem (self, index):
    "redéfinit l'accès [] séquentiel"

    # on vérifie que l'index a un sens
    if not (0 <= index < len(self)):
        raise IndexError(f"Mauvais indice {index} pour DualQueue")
    # on décide que l'index 0 correspond à l'élément le plus ancien
    # ce qui oblige à une petite gymnastique
    li = len(self.inputs)
    lo = len(self.outputs)
    if index < lo:
        return self.outputs[lo - index - 1]
    else:
        return self.inputs[li - (index-lo) - 1]

# et on affecte cette fonction à l'intérieur de la classe
DualQueue.__getitem__ = dual_queue_getitem
print(queue[0])

try:
    print(queue[5])
except IndexError as e:
    print('ERREUR',e)
    
class PlusClosure:
    """Une classe callable qui permet de faire un peu comme la 
    fonction built-in sum mais en ajoutant une valeur initiale"""
    def __init__(self, initial):
        self.initial = initial
    def __call__(self, *args):
        return self.initial + sum(args)
    
# on crée une instance avec une valeur initiale 2 pour la somme
plus2 = PlusClosure (2)
print(plus2())
print(plus2(10))
print(plus2(1,10))

    

