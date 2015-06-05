#!/usr/bin/env python

import zmq
import os

if os.path.exists('./files')==False:
    os.mkdir('./files')
filesInDir=os.listdir('./files')
exeP=0
if len(filesInDir)>0:
    print 'Estos son los proyectos ya descargados'
    print filesInDir
    print 'Desea ejecutar alguno (1) o desea descargar uno nuevo(2)?'
    while exeP<1 or exeP>2:
        exeP=input()
else:
    exeP=2

if exeP==2:
    #conecto a el servidor
    context = zmq.Context()
    print 'conectando al servidor...'
    #conecto el socket de entrada de datos
    sock = context.socket(zmq.PAIR)
    sock.connect("tcp://localhost:4545")
    #conecto el socket de envio de datos
    #envio = context.socket(zmq.REQ)
    #envio.connect("tcp://localhost:5557")
    
    #una vez conectado envio un mensaje
    msg = 'cliente conectado'
    sock.send(msg)
    #ahora recibimos el numero de proyectos
    n_proyectos = int(sock.recv())
    print (n_proyectos)
    #creo una lista para los nombres de los proyectos
    lista = []
    #recibimos los nombres de los proyectos y los guardamos en una lista
    for i in range(n_proyectos):
        lista.append(sock.recv())
    	
    
    #imprimimos la lista y esperamos a que el usuario elija un proyecto
    
    
    
    op=n_proyectos+1
    while op>n_proyectos or op<1:
        print '\n'
        for i in range(n_proyectos):
            print str(i+1)+' '+lista[i]
        print '\nElija uno de los siguientes proyectos(1..'+str(n_proyectos)+')'	
        op=input()
        
    sock.send(str(lista[op-1]))
    
    
    #recibimos el nombre del fichero
    nombre_fichero = sock.recv()
    #creamos un fichero con el nombre que recibimos
    
    #escribimos en el fichero lo que recibimos del servidor
    msg=sock.recv()
    
        
    archivo = open('./files/'+nombre_fichero,'w')
    print msg
    archivo.write(msg)
    #cerramos el fichero
    archivo.close()
else:
    print 'Estos son los proyectos ya descargados'
    print filesInDir
    fselec=0
    while fselec>len(filesInDir) or fselec<1:
        fselec=input()
    nombre_fichero=filesInDir[fselec-1]
    
execfile(nombre_fichero)





