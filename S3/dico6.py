import os
import re
import sys
from collections import defaultdict

#            { 's1': [ ( 's2',
#                        10),
#                      ( 's3',
#                        14)],
#              's2': [ ( 's3',
#                        12)],
#              's3': [ ( 's1',
#                        25)]})
#
filename=r"graph1.txt"

def graph_dict(filename):
    if os.path.exists(filename):
         with open(filename, "r", encoding='utf-8') as lines:
             try:
                 #print("***"*10)
                 dico = defaultdict(list)
                 #dico = {}
                 pattern = re.compile(r"[\w]+", re.UNICODE)
                 for line in lines :
                     sd = pattern.findall(line)
                     print("--> ", sd)
                     (a,b,c) =  sd
                     #print("(a,b,c): ",(a,b,c))
                     dico[a].append((c,int(b)))
                     #if a not in dico:
                     #    dico[a]=[]
                     #dico[a].append((c,b))
                 #print("***"*10)   
                 #for key, value in dico.items():
                 #   print(key, value)
                 #print("---"*10)
                
                 return (dico)
             except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                print ("Unexpected error:", sys.exc_info()[0])  
             except: #handle other exceptions such as attribute errors
                print ("Unexpected error:", sys.exc_info()[0])            
                print("erreur sur le fichier {}".format(filename))
    else:
        print("oups!!")

print(graph_dict(filename))
      
    