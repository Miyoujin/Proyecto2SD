import zmq

def resultadop1():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://*:4547")
    
    while True:
       r = results_receiver.recv_json()
       print "Recibo:{0}".format(r['result'])
resultadop1()