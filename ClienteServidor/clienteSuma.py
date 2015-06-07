import zmq
import random

def clienteSum():
    mult = random.randrange(1,260612)
    context = zmq.Context()
    # recieve work
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:4548")
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://localhost:4549")
    
    for i in range(10000):
        work = receiver.recv_json()
        data = work['num']
        result = { 'result' : data + mult }
        consumer_sender.send_json(result)

clienteSum()