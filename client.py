import socket
import select
import datetime
import sys
from data_check import *


def check_input(argv1, argv2, argv3):

    if argv1 != 'date' and argv1 != 'time':             # Request type check
        print('Invalid request type!')
        exit(1)

    try:
        if argv2 != socket.gethostname():               # hostname check
            return print('Wrong hostname')
    except TypeError:
        print('Unable to retrieve the hostname!')
        exit(1)

    try:
        if int(argv3) >= 64000 or int(argv3) <= 1024:   # port number check
            return print("Port number must between 1024 and 64000 and according to the port numbers of server, "
                         "please try again")
    except TypeError:
        print('Invalid port number, please try again.')
        exit(1)

    return argv1, argv2, argv3


def main(data):

    global host_name, port_num, date_or_time
    try:
        date_or_time, host_name, port_num = check_input(data[0], data[1], data[2])
    except ValueError:
        print('Invalid input!')
        exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client_address = (socket.gethostname(), 5010)


    message = bytearray()
    message.append(0x49)            # Add Magic number
    message.append(0x7E)
    message.append(0x00)            # Add PacketType
    message.append(0x01)

    if date_or_time == 'date':
        message.append(0x00)
        message.append(0x01)
    elif date_or_time == 'time':
        message.append(0x00)
        message.append(0x02)

    sock.sendto(message, (host_name, int(port_num)))

    sock.bind(client_address)

    received_data = sock

    rd, wd, ex = select.select(received_data, [], [])

    while 1:
        for received_socket in rd:
            data = received_socket.recvfrom(1024)

            if responseLen_check(data) == 1:
                if response_pacType_check(data) == 1:



if __name__ == '__main__':
    argvs = sys.argv[1:]
    main(argvs)




