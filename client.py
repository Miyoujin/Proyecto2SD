#!/usr/bin/env python

import zmq
#conecto a el servidor
context = zmq.Context()
print 'conectando al servidor...'
#conecto el socket de entrada de datos
sock = context.socket(zmq.REQ)
sock.connect("tcp://localhost:5556")
#conecto el socket de envio de datos
#envio = context.socket(zmq.REQ)
#envio.connect("tcp://localhost:5557")

#una vez conectado envio un mensaje
msg = 'cliente conectado'
sock.send(msg)

#ahora recibimos el numero de proyectos
n_proyectos = sock.recv()
print (n_proyectos)
#creo una lista para los nombres de los proyectos
lista = []
#recibimos los nombres de los proyectos y los guardamos en una lista
for i in range(n_proyectos):
	lista.append(sock.recv())

#imprimimos la lista y esperamos a que el usuario elija un proyecto
print 'Elija uno de los siguientes proyectos e introduzca su correspondiente nombre'	
print lista
sock.send(input())

#recibimos el nombre del fichero
nombre_fichero = sock.recv()
#creamos un fichero con el nombre que recibimos
archivo = open(nombre_fichero,'w')
#escribimos en el fichero lo que recibimos del servidor
archivo.write(sock.recv())
#cerramos el fichero
archivo.close()





