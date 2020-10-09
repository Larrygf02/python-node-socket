import socket

server_socket = socket.socket()
server_socket.bind(('localhost', 8000))
server_socket.listen(5)

while True:
    conexion, addr = server_socket.accept()
    print("Nueva conexion establecida")
    print(addr)

    peticion = conexion.recv(1024)
    print(peticion)
    conexion.send(b"Hola, te saludo desde el servidor!")
    conexion.close()
