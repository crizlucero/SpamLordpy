import re
from os import listdir
from os.path import isfile, join

def CorregirTelefono(telefono):
    telefono = telefono.replace(" ",'')
    telefono = telefono.replace('-','')
    if re.match('\([0-9]*\)',telefono):
        telefono = telefono.replace("(",'')
        telefono = telefono.replace(")",'')

    return telefono

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
        h.seek(0)
    c.close()
    h.seek(0)
    for line in t:
        for row in h:
            line = line.strip('\n')
            m = re.findall(line,row)
            if len(m) > 0:
                for tel in m:
                    tel = CorregirTelefono(tel)
                    if(not tel in telefonos):
                        telefonos.append(tel)
                #print m[0]
                count2 = count2 + 1
        line = None
        h.seek(0)
    t.close()
telefonos.sort()
cw = open("Datos.dat",'w')
for correo in correos:
    cw.write(correo + '\n')
for telefono in telefonos:
    cw.write(telefono + "\n")
cw.close()

