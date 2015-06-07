import zmq

def resultadoSum():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://*:4549")
    
    while True:
       r = results_receiver.recv_json()
       print "Recibo:{0}".format(r['result'])
resultadoSum()