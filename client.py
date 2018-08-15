import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('Zhis-Mac.local', 5010))

message = "hello world"

message_encode = message.encode('utf-8')


sock.sendto(message_encode, ('Zhis-Mac.local', 5002))

