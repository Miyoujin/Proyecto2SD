#!/usr/bin/python2

import zmq
import os
import socket

def server():
    # Levantamos el contexto de ZMQ y el socket REP
    context = zmq.Context()
    sock = context.socket(zmq.PAIR)
    sock.bind('tcp://*:4545')

    #Definimos los proyectos
    proyects = ['proyecto1', 'proyecto2', 'proyecto3']
    files = ['p1.py', 'p2.py', 'p3.py']
    #Inicia el servidor
    while True:
       try:
            #Envia la lista de proyectos
    	    connect = sock.recv()
    	    print connect
    	    print 'hola'
    	    sock.send(str(len(proyects)))
    	    
    	    for p in proyects:
                 sock.send(p)
    
            #Recive el nombre del proyecto seleccionado
    	    msg = sock.recv()
    	    
            #Alhama modifica esto
    	    pos=proyects.index(msg)
    	    file = files[pos]
    	    fn = open(file, 'rb')
    
    	    sock.send(file)
    	    sock.send(fn.read())
       except ValueError:
           print 'Ha ocurrido un error'
           sock.send('')

if __name__ == '__main__':
    server()
