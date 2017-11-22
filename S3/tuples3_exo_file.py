from pathlib import Path
import os

ifilename=r"in_file_exo.txt"
ofilename=r"out_file_exo.txt"

def comptage(in_filename, out_filename):
    if os.path.exists(in_filename):
        with open(in_filename, "r", encoding='utf-8') as lines_in_file,\
         open(out_filename, "w", encoding='utf-8') as lines_out_file:
            try:
                i=1
                sep=":"
                oline=None
                for iline in line_in_file:
                    oline=""
                    print(line, end='')
                    lines_out_file.write("{}{}{}".format(i,sep,iline))
                    
            except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            except: #handle other exceptions such as attribute errors
                print ("Unexpected error:", sys.exc_info()[0])            
                print("erreur sur le fichier{}".format(ifilename))

comptage(ifilename,ofilename)