import os
import sys
import re

ifilename=r"in_file_exo.txt"
ofilename=r"out_file_exo.txt"

def comptage(in_filename, out_filename):
    if os.path.exists(in_filename):
        with open(in_filename, "r", encoding='utf-8') as lines_in_file:
            with open(out_filename, "w", encoding='utf-8') as lines_out_file:
                try:
                    i=1
                    sep=":"
                    oline=None
                    #for iline, oline in zip(lines_in_file,lines_out_file) :
                    #print(f"{lines_out_file}")
                    for iline in lines_in_file :
                        pattern = re.compile(r"([\b\w\-\'\b]+)", re.UNICODE)
                        sd = pattern.findall(iline)
                        cwords = len(sd)
                        #print(cwords)
                        pattern = re.compile(r"([-\w\',;\.\:\s\n\r])", re.UNICODE)
                        sd = pattern.findall(iline)
                        ccharacters = len(sd)
                        #print(ccharacters)
                        print(iline, end='')
                        lines_out_file.write(f"{i}{sep}{cwords}{sep}{ccharacters}{sep}{iline}")
                        i+=1
                        
                except IOError as e:
                    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                    print ("Unexpected error:", sys.exc_info()[0])  
                except: #handle other exceptions such as attribute errors
                    print ("Unexpected error:", sys.exc_info()[0])            
                    print("erreur sur le fichier {}".format(ifilename))

comptage(ifilename,ofilename)