import os
import re
import sys


filename=r"graph1.txt"

def graph_dict(filename):
    if os.path.exists(filename):
         with open(filename, "r", encoding='utf-8') as lines:
             try:
                 print("***"*10)
                 #dico = {}
                 #pattern = re.compile(r"[\w]{1} [0-9]+ [\w]{1}", re.UNICODE)
                 pattern = re.compile(r"[\w]{1} [0-9]+ [\w]{1}", re.UNICODE)
                 for line in lines :
                     print(line)
                     sd = pattern.search(line)
                     print(sd, ', ', type(sd))
                     print(sd.groupdict())
                     #dico.append
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