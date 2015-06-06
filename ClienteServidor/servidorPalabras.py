#!usr/bin/python

import zmq
import random

context = zmq.Context()
envio = context.socket(zmq.PUSH)

envio.bind("tcp://*:5557")
print "Hay que esperar que los workers se inicien"
print "Se inicia la transmision del trabajo..."

while True:

    cadenas = ['hola','aloha','hello','buenas noches','buenas tardes','buenos dias','bienvenido']
    
    for i in range(len(cadenas)):
        cadena = cadenas[i]
        envio.send(cadena)
        print "Enviando: {0}".format(cadena)
