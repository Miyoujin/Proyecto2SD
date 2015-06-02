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

    #Inicia el servidor
    while True:
        #Envía la lista de proyectos
        sock.send(proyects)

        #Recive el nombre del proyecto seleccionado
        msg = sock.recv()
        if msg not in proyects:
            sock.send('No ha elegido un proyecto valido')
        else:
            #Alhama modifica esto
            fn = open(msg, 'rb')
            stream = True

            while stream:
                stream = fn.read(128)
                if stream:
                    sock.send(stream, zmq.SNDMORE)
                else:
                    sock.send(stream)

if __name__ == '__main__':
    server()
