
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

extended = [[228148700, 49.6896, -4.114284, '2013-10-08T21:51:00', 'DAYTONA', 'FR', '', 'ROSCOFF'], [305686000, 49.19304, -5.034783, '2013-10-08T21:50:00', 'INDUSTRIAL KELLY', 'AG', '', 'ESBJERG'], [228109000, 48.21843, -4.996732, '2013-10-08T21:51:00', 'KAN AN AEL', 'FR', '', ''], [477188500, 49.07116, -4.831073, '2013-10-08T21:51:00', 'ANSAC PRIDE', 'HK', '', 'BILBAO']]

abbreviated =[[228109000, 48.18373, -5.049758, '2013-10-08T22:58:00'], [477188500, 49.19563, -4.531655, '2013-10-08T22:58:00'], [227115520, 48.09115, -4.333058, '2013-10-08T22:55:00'], [228240900, 47.19841, -2.723277, '2013-10-08T22:55:00']]



def diff(extended, abbreviated):
    try:
        ext_ensemble = set()
        abb_ensemble = set()
        ext_dico = {}
        
        set_name_isext_not_abb = set()
        set_name_isext_isabb = set()
        set_id_isabb_not_ext = set()

        for ext_line in extended :
            #print(ext_line)
            (id, position_etendu, position_abrege, gmt_time, nom_bateau, code_pays, *truc) =  ext_line
            ext_ensemble.add((id, nom_bateau) )
            ext_dico[id]= nom_bateau
        for abb_line in abbreviated :
            #print(abb_line)
            (id, position_etendu, position_abrege, gmt_time) =  abb_line
            if id in ext_dico:
                abb_ensemble.add( (id, ext_dico.get(id)))
            else:
                abb_ensemble.add( (id, ''))
        #l'ensemble (set) des noms des bateaux présents dans extended mais pas dans abbreviated: set_name_isext_not_abb
        #l'ensemble des noms des bateaux présents dans extended et dans abbreviated: set_name_isext_isabb
        for id, name in ext_ensemble - abb_ensemble:
            print("->", id, ", ", name)
            set_name_isext_not_abb.add(name)
        #print(ext_ensemble & abb_ensemble)
        for id, name in ext_ensemble  & abb_ensemble:
            print("-->", id, ", ", name)
            set_name_isext_isabb.add(name)
        #print(abb_ensemble - ext_ensemble)
        for id, name in  abb_ensemble - ext_ensemble:
            print("--->", id, ", ", name)
            set_id_isabb_not_ext.add(id)
        return (set_name_isext_not_abb, set_name_isext_isabb, set_id_isabb_not_ext)         
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        print ("Unexpected error:", sys.exc_info()[0])  
    except: #handle other exceptions such as attribute errors
        print ("Unexpected error:", sys.exc_info()[0])            
        print("erreur sur les fichiers {} {}".format(file_extended, filename_abbreviated))
    return 


print(diff(extended, abbreviated)) 
