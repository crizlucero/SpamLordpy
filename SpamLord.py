import re
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("MIT Sloan Staff Directory") if isfile(join("MIT Sloan Staff Directory",f))]

#abrir Archivo
for files in onlyfiles:
    c = open("Correos.txt","r")
    t = open("Telefonos.txt","r")
    h = open("MIT Sloan Staff Directory/"+files)
    #Correos
    for line in c:
        for row in h:
            line = line.strip('\n')
            m = re.findall(line,row)
            if len(m) > 0:
                print m
        line = None
    c.close()
    h.seek(0)
    for line in t:
        for row in h:
            line = line.strip('\n')
            m = re.findall(line,row)
            if len(m) > 0:
                print m
        line = None
    t.close()



