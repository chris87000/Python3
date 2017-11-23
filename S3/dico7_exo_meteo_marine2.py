import os
import re
import sys
from collections import defaultdict
from pprint import pprint

#meteo marine, exo intermediaire

extended = [ [ 992271012, 47.64744,-3.509282,'2013-10-08T21:50:00', 'PENMEN', 'FR', '', ''],
            [ 227254910, 49.94479, -5.137455,'2013-10-08T21:51:00','LAURELINE','FR','','CHERBOURG'],
            [ 227844000, 47.23206, -2.913887, '2013-10-08T21:51:00','NEPTUNE III','FR', '',''],
            [ 255801560, 49.3815, -4.412167, '2013-10-08T21:51:00', 'AUTOPRIDE', 'PT', '',  'ZEEBRUGGE']]
    
abbreviated = [ [ 227254910, 49.91799, -5.315172,'2013-10-08T22:59:00'],
               [ 255801560, 49.25383, -4.784833, '2013-10-08T22:59:00'],
               [ 992271012, 47.64748, -3.509307,'2013-10-08T22:56:00'],
               [ 227844000, 47.13057, -3.126982,'2013-10-08T22:58:00']]

#===============================================================================
# id -> [ nom_bateau, code_pays, position_etendu, position_abrege ]
# position_etendu et position_abrege :  (latitude, longitude, date_heure)
# { 227254910: [ 'LAURELINE',
#                'FR',
#                ( 49.94479,
#                  -5.137455,
#                  '2013-10-08T21:51:00'),
#                ( 49.91799,
#                  -5.315172,
#                  '2013-10-08T22:59:00')],
#   227844000: [ 'NEPTUNE '
#                'III',
#                'FR',
#                ( 47.23206,
#                  -2.913887,
#                  '2013-10-08T21:51:00'),
#                ( 47.13057,
#                  -3.126982,
#                  '2013-10-08T22:58:00')],
#   255801560: [ 'AUTOPRIDE',
#                'PT',
#                ( 49.3815,
#                  -4.412167,
#                  '2013-10-08T21:51:00'),
#                ( 49.25383,
#                  -4.784833,
#                  '2013-10-08T22:59:00')],
#   992271012: [ 'PENMEN',
#                'FR',
#                ( 47.64744,
#                  -3.509282,
#                  '2013-10-08T21:50:00'),
#                ( 47.64748,
#                  -3.509307,
#                  '2013-10-08T22:56:00')]}
#===============================================================================

    

  
def merge(extended_tab, abbreviated_tab):
    #dico = defaultdict(list)
    dico = {}
    for tab in extended_tab:
        #id -> [ nom_bateau, code_pays, position_etendu, position_abrege ]
        # [ 227254910, 49.94479, -5.137455,'2013-10-08T21:51:00','LAURELINE','FR','','CHERBOURG']
        (id, position_etendu, position_abrege, gmt_time, nom_bateau, code_pays, truc, port_attache) =  tab
        #print((id, position_etendu, position_abrege, gmt_time, nom_bateau, code_pays, truc, port_attache))
        if id not in dico:
            dico[id]= [nom_bateau, code_pays,(position_etendu, position_abrege, gmt_time) ]
    return(dico)
             
pprint(merge(extended, abbreviated))

#pprint(zip(extended, abbreviated))
      