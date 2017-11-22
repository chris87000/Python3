import os
import re
import sys
from collections import defaultdict

filename=r"graph1.txt"

def graph_dict(filename):
    if os.path.exists(filename):
         with open(filename, "r", encoding='utf-8') as lines:
             try:
                 print("***"*10)
                 dico = defaultdict(list)
                 the_tuple=()
                 pattern = re.compile(r"[\w]+", re.UNICODE)
                 for line in lines :
                     sd = pattern.findall(line)
                     the_tuple = tuple(sd) 
                     #print(sd, ', ', type(sd))
                     print(the_tuple, ', ', type(the_tuple))
                     for x, y in the_tuple:
                        dico[x].append(y)
                 print(dico)
                 print("***"*10)    
             except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                print ("Unexpected error:", sys.exc_info()[0])  
             except: #handle other exceptions such as attribute errors
                print ("Unexpected error:", sys.exc_info()[0])            
                print("erreur sur le fichier {}".format(filename))
    else:
        print("oups!!")

graph_dict(filename)