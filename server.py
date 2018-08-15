import select
import socket
from data_check import *

sock_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

a = magicNo_check("0x1234")
print(a)

print("FOR PORT NUMBER:", port_num_1, " all the info will be displayed in English")
print("FOR PORT NUMBER:", port_num_2, " all the info will be displayed in English")
print("FOR PORT NUMBER:", port_num_3, " all the info will be displayed in English")

address_1 = ('Zhis-Mac.local', port_num_1)  # In English
address_2 = ('Zhis-Mac.local', port_num_2)  # In Te reo Maori
address_3 = ('Zhis-Mac.local', port_num_3)  # In German

sock_1.bind(address_1)
sock_2.bind(address_2)
sock_3.bind(address_3)

inputList = [sock_1, sock_2, sock_3]

rd, wd, ex = select.select(inputList, [], [])
select.select(inputList, [], [])

while 1:

    #info_eng = bytearray(sock_1.recvfrom(1024))

    #data = bytearray(sock_1.recvfrom(1024)[0].to_array(6, 'big'))


    for received_socket in rd:
        if received_socket == sock_1:
            ''' Englis '''
            if requset == 1:
                '''data'''
            elif request == 2:
                '''time'''
        elif received_socket == sock_3:
            ''' Moroi'''

    data ,(ipaddress, portnumber) = sock_1.recvfrom(1024)
    ip_add, port_num = receive_from
    print(port_num)
    sock_2.recvfrom(1024)
    sock_3.recvfrom(1024)



