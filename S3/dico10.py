
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

filename =r"data/setref1.txt"
def read_set(filename):
    with open(filename, "r", encoding='utf-8') as lines:
        try:
            ensemble = set()
            tab=[]
            for line in lines :
                 pattern = re.compile(r"([\b\d\b]+)", re.UNICODE)
                 sd = pattern.findall(line)
                 #print(sd, "," , type(sd))
                 tab.append(sd[0])
            tab.sort()
            ensemble = set(tab)
            print(tab, "," , type(tab))
            print("ensemble:\n ", ensemble)
            return ensemble
        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            print ("Unexpected error:", sys.exc_info()[0])  
        except: #handle other exceptions such as attribute errors
            print ("Unexpected error:", sys.exc_info()[0])            
            print("erreur sur le fichier {}".format(ifilename))
    return 


read_set(filename) 
