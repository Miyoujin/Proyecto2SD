import zmq
from time import sleep
context=zmq.Context()
recepcion=context.socket(zmq.PULL)
recepcion.connect("tcp://localhost:5557")
envio=context.socket(zmq.PUSH)
envio.connect("tcp://localhost:5558")
while True:
	cadena=recepcion.recv()
	print "Proceso:{0}".format(cadena)
	envio.send(cadena.upper())
	sleep(1)