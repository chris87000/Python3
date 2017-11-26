
# Exercice - niveau basique
# read set ...
#===============================================================================
# 4615
#  12
#  9228
# 6158
# 12
#===============================================================================

import os
import sys
from pprint import pprint
import re

filename_reference =r"data/setref1.txt"
filename =r"data/setsample1.txt"

def search_in_set(filename_reference, filename):
    with open(filename_reference, "r", encoding='utf-8') as lines_ref:
        with open(filename, "r", encoding='utf-8') as lines:
            try:
                tabfinal=[]
                ensemble = set()
                tabref=[]
                for line_ref in lines_ref :
                     pattern = re.compile(r"([\b\d\b]+)", re.UNICODE)
                     sd = pattern.findall(line_ref)
                     #print(sd, "," , type(sd))
                     tabref.append(sd[0])
                tabref.sort()
                ensemble = set(tabref)
                pprint(ensemble)
                for line in lines:
                    pattern = re.compile(r"([\b\d\b]+)", re.UNICODE)
                    sd = pattern.findall(line)
                    if sd[0] in ensemble:
                        tabfinal.append((sd[0],True))
                    else:
                        tabfinal.append((sd[0],False))
                return tabfinal         
            except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                print ("Unexpected error:", sys.exc_info()[0])  
            except: #handle other exceptions such as attribute errors
                print ("Unexpected error:", sys.exc_info()[0])            
                print("erreur sur le fichier {}".format(ifilename))
    return 


print(search_in_set(filename_reference, filename)) 
