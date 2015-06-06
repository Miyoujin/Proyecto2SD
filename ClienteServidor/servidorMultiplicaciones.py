import zmq

def serverMult():
    context = zmq.Context()
    sock = context.socket(zmq.PUSH)
    sock.bind('tcp://*:4546')
    # Start your result manager and workers before you start your producers
    while True:
        for x in xrange(20000):
            message = { 'num' : x }
            sock.send_json(message)

if __name__ == '__main__':
    serverMult()