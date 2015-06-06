#!/usr/bin/python2

import zmq
import os
import socket

def server():
    # Levantamos el contexto de ZMQ y el socket REP
    context = zmq.Context()
    sock = context.socket(zmq.PAIR)
    #Definimos los proyectos
    sock.bind('tcp://*:4545')
    f = open('proyectos.txt')
    proyects = f.read()
    f.close();
    proyects = proyects.split('\n')
    print proyects
    f = open('fproyectos.txt')
    files = f.read()
    f.close();
    files = files.split('\n')
    #Inicia el servidor
    while True:
       try:
            #Envia la lista de proyectos
    	    connect = sock.recv()
    	    print connect
    	    f = open('proyectos.txt')
            proyects = f.read()
            f.close();
            proyects = proyects.split('\n')
            print proyects
            f = open('fproyectos.txt')
            files = f.read()
            f.close();
            files = files.split('\n')
    	    sock.send(str(len(proyects)))
    	    
    	    for p in proyects:
                 sock.send(p)
    
            #Recive el nombre del proyecto seleccionado
    	    msg = sock.recv()
    	    
            #Alhama modifica esto
    	    pos=proyects.index(msg)
    	    file = files[pos]
    	    if os.path.exists('files'+file)==False:
    	        fn = open('./ClienteServidor/'+file, 'rb')
    
    	    sock.send(file)
    	    sock.send(fn.read())
       except ValueError:
           print 'Ha ocurrido un error'
           sock.send('')

if __name__ == '__main__':
    server()
