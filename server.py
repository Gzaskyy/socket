import select
import socket
import sys
import datetime
from data_check import *
from convert import *


def check_port(argv1, argv2, argv3):
    try:
        if int(argv1) >= 64000 or int(argv1) <= 1024:
            return print("Port number_1 must between 1024 and 64000, please try again")
    except ValueError:
        print("Not a valid port1, please try again.")
        exit(1)

    try:
        if int(argv2) >= 64000 or int(argv2) <= 1024:
            return print("Port number_2 must between 1024 and 64000, please try again")
    except ValueError:
        print("Not a valid port2, please try again.")
        exit(1)

    try:
        if int(argv3) >= 64000 or int(argv3) <= 1024:
            return print("Port number_3 must between 1024 and 64000, please try again")
    except ValueError:
        print("Not a valid port3, please try again.")
        exit(1)

    if int(argv1) != int(argv2) and int(argv2) != int(argv3) and int(argv1) != int(argv3):
        return int(argv1), int(argv2), int(argv3)


def main(ports):
    try:
        port_1, port_2, port_3 = check_port(ports[0], ports[1], ports[2])
    except TypeError:
        print('Error occurred!')
        exit(1)

    sock_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("FOR PORT NUMBER:", port_1, ": all the info will be displayed in English")
    print("FOR PORT NUMBER:", port_2, ": all the info will be displayed in Te reo Maori")
    print("FOR PORT NUMBER:", port_3, ": all the info will be displayed in German")

    address_1 = ('Zhis-Mac.local', port_1)  # In English
    address_2 = ('Zhis-Mac.local', port_2)  # In Te reo Maori
    address_3 = ('Zhis-Mac.local', port_3)  # In German

    sock_1.bind(address_1)
    sock_2.bind(address_2)
    sock_3.bind(address_3)

    inputList = [sock_1, sock_2, sock_3]

    rd, wd, ex = select.select(inputList, [], [])
    # select.select(inputList, [], [])
    while 1:

        global time_or_date

        for received_socket in rd:

            response_data = bytearray()

            data, (ipaddress, portnumber) = received_socket.recvfrom(1024)
            if requestLen_check(data) == 1:
                if magicNo_check(data) == 1:
                    response_data.append(data[0])
                    response_data.append(data[1])
                    if package_type_check(data) == 1:
                        response_data.append(data[2])
                        response_data.append(data[3])
                        if request_type_check(data) == 1:
                            """Date"""
                            response_data.append(data[4])
                            response_data.append(data[5])
                            time_or_date = 1
                        elif request_type_check(data) == 2:
                            """Time"""
                            response_data.append(data[4])
                            response_data.append(data[5])
                            time_or_date = 2
                        else:
                            return print("Wrong language type request")
                    return print("Wrong package type")
                else:
                    print("Error magic number")
            else:
                print("packet length error")
            if time_or_date == 1:
                response_data.append(int_to_2byte(now.year)[0])
                response_data.append(int_to_2byte(now.year)[1])


if __name__ == '__main__':
    argvs = sys.argv[1:]
    main(argvs)
    now = datetime.datetime.now()
