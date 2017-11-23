import os
import re
import sys
from collections import defaultdict

#meteo marine

tabs = [ [ 227254910,
                  49.91799,
                  -5.315172,
                  '2013-10-08T22:59:00'],
                [ 255801560,
                  49.25383,
                  -4.784833,
                  '2013-10-08T22:59:00'],
                [ 992271012,
                  47.64748,
                  -3.509307,
                  '2013-10-08T22:56:00'],
                [ 227844000,
                  47.13057,
                  -3.126982,
                  '2013-10-08T22:58:00']]
def index(tablox):
    #dico = defaultdict(list)
    dico = {}
    for tab in tablox:
        (a,*b) =  tab
        print((a,*b))
        #dico[a].append((a,*b))
        if a not in dico:
            dico[a]=[a,*b]
        #liste = list((a,*b))
        #be = zip(*b)
        #dico[a].append(liste)
    return(dico)
             
print(index(tabs))
      