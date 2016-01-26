import re
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("MIT Sloan Staff Directory") if isfile(join("MIT Sloan Staff Directory",f))]
count1, count2 = 0,0
correos = []
telefonos = []
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
                for mail in m:
                    if(not mail in correos):
                        correos.append(mail)
                #print m[0]
                count1 = count1 + 1
        line = None
    c.close()
    h.seek(0)
    for line in t:
        for row in h:
            line = line.strip('\n')
            m = re.findall(line,row)
            if len(m) > 0:
                for tel in m:
                    if(not tel in telefonos):
                        telefonos.append(tel)
                #print m[0]
                count2 = count2 + 1
        line = None
    t.close()
print len(correos)
print len(telefonos)
print count1
print count2


