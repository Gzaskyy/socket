import select
import socket
from data_check import *

import sys


def check_port(argv1, argv2, argv3):
    try:
        if int(argv1) >= 64000 or int(argv1) <= 1024:
            return print("Port number_1 must between 1024 and 64000, please try again")

    except ValueError:
        print("Not a valid port1, please try again.")

    try:
        if int(argv2) >= 64000 or int(argv2) <= 1024:
            return print("Port number_2 must between 1024 and 64000, please try again")
    except ValueError:
        print("Not a valid port2, please try again.")

    try:
        if int(argv3) >= 64000 or int(argv3) <= 1024:
            return print("Port number_3 must between 1024 and 64000, please try again")
    except ValueError:
        print("Not a valid port3, please try again.")

    return int(argv1), int(argv2), int(argv3)


def main(ports):

    port_1, port_2, port_3 = check_port(ports[0], ports[1], ports[2])
    sock_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("FOR PORT NUMBER:", port_1, " : all the info will be displayed in English")
    print("FOR PORT NUMBER:", port_2, " : all the info will be displayed in Te reo Maori")
    print("FOR PORT NUMBER:", port_3, " : all the info will be displayed in German")

    address_1 = ('Zhis-Mac.local', port_1)  # In English
    address_2 = ('Zhis-Mac.local', port_2)  # In Te reo Maori
    address_3 = ('Zhis-Mac.local', port_3)  # In German

    sock_1.bind(address_1)
    sock_2.bind(address_2)
    sock_3.bind(address_3)

    inputList = [sock_1, sock_2, sock_3]

    rd, wd, ex = select.select(inputList, [], [])
    select.select(inputList, [], [])
    while 1:

        # info_eng = bytearray(sock_1.recvfrom(1024))

        # data = bytearray(sock_1.recvfrom(1024)[0].to_array(6, 'big'))

        # for received_socket in rd:
        #     if received_socket == sock_1:
        #         ''' Englis '''
        #         if requset == 1:
        #             '''data'''
        #         elif request == 2:
        #             '''time'''
        #     elif received_socket == sock_3:
        #         ''' Moroi'''

        data, (ipaddress, portnumber) = sock_1.recvfrom(1024)
        sock_2.recvfrom(1024)
        sock_3.recvfrom(1024)


if __name__ == '__main__':
    argvs = sys.argv[1:]
    main(argvs)

