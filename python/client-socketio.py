import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection stablished')

@sio.event
def my_message(data):
    print('message recieved with ', data)
    sio.emit('data', {'response': 'my response'})

@sio.event
def disconnet():
    print('disconnect from server')

sio.connect('http://localhost:3000')
my_message('hello')
sio.wait()