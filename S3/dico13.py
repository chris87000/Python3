
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
import json

exfilename=r"data/marine-e2-ext.json"
abfilename=r"data/marine-e2-abb.json"

def diff(extended, abbreviated):
    
    with open(extended, "r", encoding="utf-8") as feed:
        extended_full = json.load(feed)
    
    with open(abbreviated, "r", encoding="utf-8") as feed:
        abbreviated_full = json.load(feed)
        
    try:
        ext_ensemble = set()
        abb_ensemble = set()
        ext_dico = {}
        
        set_name_isext_not_abb = set()
        set_name_isext_isabb = set()
        set_id_isabb_not_ext = set()

        for ext_line in extended_full :
            #print(ext_line)
            (id, position_etendu, position_abrege, gmt_time, nom_bateau, code_pays, *truc) =  ext_line
            ext_ensemble.add((id, nom_bateau) )
            ext_dico[id]= nom_bateau
        for abb_line in abbreviated_full :
            #print(abb_line)
            (id, position_etendu, position_abrege, gmt_time) =  abb_line
            if id in ext_dico:
                abb_ensemble.add( (id, ext_dico.get(id)))
            else:
                abb_ensemble.add( (id, ''))
        #l'ensemble (set) des noms des bateaux présents dans extended mais pas dans abbreviated: set_name_isext_not_abb
        #l'ensemble des noms des bateaux présents dans extended et dans abbreviated: set_name_isext_isabb
        for id, name in ext_ensemble - abb_ensemble:
            #print("->", id, ", ", name)
            set_name_isext_not_abb.add(name)
        print(len(set_name_isext_not_abb))
        #print(ext_ensemble & abb_ensemble)
        for id, name in ext_ensemble  & abb_ensemble:
            #print("-->", id, ", ", name)
            set_name_isext_isabb.add(name)
        print(len(set_name_isext_isabb))
        #print(abb_ensemble - ext_ensemble)
        for id, name in  abb_ensemble - ext_ensemble:
            #print("--->", id, ", ", name)
            set_id_isabb_not_ext.add(id)
        print(len(set_id_isabb_not_ext))
        return (set_name_isext_not_abb, set_name_isext_isabb, set_id_isabb_not_ext)         
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        print ("Unexpected error:", sys.exc_info()[0])  
    except: #handle other exceptions such as attribute errors
        print ("Unexpected error:", sys.exc_info()[0])            
        print("erreur sur les fichiers {} {}".format(file_extended, filename_abbreviated))
    return 



print(diff(exfilename, abfilename)) 
