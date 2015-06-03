#!/usr/bin/python2

import zmq
import os

def server():
    # Levantamos el contexto de ZMQ y el socket REP
    context = zmq.Context(1)
    sock = context.socket(zmq.REP)
    sock.bind('tcp://*:4545')

    #Definimos los proyectos
    proyects = ['proyecto1', 'proyecto2', 'proyecto3']
    files = ['p1.py', 'p2.py', 'p3.py']
    #Inicia el servidor
    while True:
        #Envia la lista de proyectos
	connect = sock.recv()
	
	for p in proyects:
            sock.send(p)

        #Recive el nombre del proyecto seleccionado
        msg = sock.recv()
        if msg not in proyects:
            sock.send('No ha elegido un proyecto valido')
        else:
            #Alhama modifica esto
            pos=proyects.index(msg)
            file = files[pos]
            fn = open(file, 'rb')
            stream = True
            sock.send(file)
            while stream:
                stream = fn.read(128)
                if stream:
                    sock.send(stream, zmq.SNDMORE)
                else:
                    sock.send(stream)

if __name__ == '__main__':
    server()
