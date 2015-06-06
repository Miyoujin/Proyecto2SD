#!/usr/bin/python
import zmq

context=zmq.Context()
recepcion=context.socket(zmq.PULL)
recepcion.bind("tcp://*:5558")

while True:
	mensaje=recepcion.recv()
	print "Recibo:{0}".format(mensaje)
