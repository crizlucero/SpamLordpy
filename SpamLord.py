#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re
from os import listdir
from os.path import isfile, join


def CorregirTelefono(tels):
    tels = tels.replace(" ", '')
    tels = tels.replace('-', '')
    if re.match('\([0-9]*\)', tels):
        tels = tels.replace("(", '')
        tels = tels.replace(")", '')

    return tels


onlyfiles = [f for f in listdir("MIT Sloan Staff Directory") if isfile(join("MIT Sloan Staff Directory", f))]
correos = []
telefonos = []
#abrir Archivo
for files in onlyfiles:
    c = open("Correos.txt", "r")
    t = open("Telefonos.txt", "r")
    h = open("MIT Sloan Staff Directory/"+files)
    #Correos
    for line in c:
        for row in h:
            line = line.strip('\n')
            m = re.findall(line, row)
            if len(m) > 0:
                for mail in m:
                    if mail not in correos:
                        correos.append(mail)
        line = None
        h.seek(0)
    c.close()
    h.seek(0)
    for line in t:
        for row in h:
            line = line.strip('\n')
            m = re.findall(line, row)
            if len(m) > 0:
                for tel in m:
                    tel = CorregirTelefono(tel)
                    if tel not in telefonos:
                        telefonos.append(tel)
        line = None
        h.seek(0)
    t.close()
telefonos.sort()
cw = open("Datos.dat", 'w')
cw.write(u'-----------------------------CORREOS-----------------------------\n')
for correo in correos:
    cw.write(correo[0] + '\n')
cw.write("Total: " + str(len(correos)))
cw.write(u'\n----------------------------TELEFONOS----------------------------\n')
for telefono in telefonos:
    cw.write("(" + telefono[:3] + ") " + telefono[3:6] + "-" + telefono[6:] + "\n")
cw.write("Total: " + str(len(telefonos)))
cw.close()

