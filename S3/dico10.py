
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

filename =r"data/setref1.txt"
def read_set(filename):
    with open(extended_file, "r", encoding='utf-8') as lines:
        try:
            for line in lines :
                print("")
                
            return 
        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            print ("Unexpected error:", sys.exc_info()[0])  
        except: #handle other exceptions such as attribute errors
            print ("Unexpected error:", sys.exc_info()[0])            
            print("erreur sur le fichier {}".format(ifilename))
    return  
