import select
import socket
import sys
import datetime
from data_check import *
from convert import *
from language_textual import *


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

    print("FOR PORT NUMBER:", port_1, ": all info will be displayed in English")
    print("FOR PORT NUMBER:", port_2, ": all info will be displayed in Te reo Maori")
    print("FOR PORT NUMBER:", port_3, ": all info will be displayed in German")

    address_1 = (socket.gethostname(), int(port_1))  # In English
    address_2 = (socket.gethostname(), int(port_2))  # In Te reo Maori
    address_3 = (socket.gethostname(), int(port_3))  # In German

    sock_1.bind(address_1)
    sock_2.bind(address_2)
    sock_3.bind(address_3)

    inputList = [sock_1, sock_2, sock_3]

    rd, wd, ex = select.select(inputList, [], [])
    # select.select(inputList, [], [])
    while 1:

        for received_socket in rd:

            response_data = bytearray()
            time_or_date = ''

            data, (ipaddress, portnumber) = received_socket.recvfrom(1024)

            if received_socket == sock_1:                                # Language selection
                language_selection = 1
            elif received_socket == sock_2:
                language_selection = 2
            elif received_socket == sock_3:
                language_selection = 3
            else:
                print("Wrong language selection")
            if requestLen_check(data) == 1:                 # DT_request length check
                if magicNo_check(data) == 1:                # DT_request MagicNo check
                    response_data.append(data[0])
                    response_data.append(data[1])
                    if package_type_check(data) == 1:       # DT_request package type check
                        response_data.append(0x00)          # DT_response type added
                        response_data.append(0x02)
                        if request_type_check(data) == 1:   # DT_request time or date selection
                            time_or_date = 'date'
                        elif request_type_check(data) == 2:
                            time_or_date = 'time'
                            if language_selection == 1:     # Language 1:English 2:Mori 3:German
                                response_data.append(0x00)
                                response_data.append(0x01)
                            elif language_selection == 2:
                                response_data.append(0x00)
                                response_data.append(0x02)
                            elif language_selection == 3:
                                response_data.append(0x00)
                                response_data.append(0x03)
                    else:
                        print("Wrong package type")
                        exit(1)
                else:
                    print("Error magic number")
                    exit(1)
            else:
                print("packet length error")
                exit(1)

            """Add year, month, day, hour, minute to byte array"""
            sys_now = datetime.datetime.now()
            response_data += int(bin(sys_now.year)[2:].zfill(16), 2).to_bytes(2, 'big')  # Add year
            response_data.append(sys_now.month)
            response_data.append(sys_now.day)
            response_data.append(sys_now.hour)
            response_data.append(sys_now.minute)

            """generate requested text type"""
            if time_or_date == 'date' and language_selection == 1:      # English date
                if len(to_english_date()) <= 255:
                    response_data.append(len(to_english_date()))
                    response_data += to_english_date()
                else:
                    print("Text length overflow!")
            elif time_or_date == 'time' and language_selection == 1:    # English time
                if len(to_english_time()) <= 255:
                    response_data.append(len(to_english_time()))
                    response_data += to_english_date()
                else:
                    print("Text length overflow!")
            elif time_or_date == 'date' and language_selection == 2:    # Mori date
                if len(to_mori_date()) <= 255:
                    response_data.append(len(to_mori_date()))
                    response_data += to_mori_date()
                else:
                    print("Text length overflow!")
            elif time_or_date == 'time' and language_selection == 2:    # Mori time
                if len(to_mori_time()) <= 255:
                    response_data.append(len(to_mori_time()))
                    response_data += to_mori_time()
                else:
                    print("Text length overflow!")
            elif time_or_date == 'date' and language_selection == 3:    # German date
                if len(to_german_date()) <= 255:
                    response_data.append(len(to_german_date()))
                    response_data += to_german_date()
                else:
                    print("Text length overflow!")
            elif time_or_date == 'time' and language_selection == 3:    # German time
                if len(to_german_time()) <= 255:
                    response_data.append(len(to_german_time()))
                    response_data += to_german_time()
                else:
                    print("Text length overflow!")

            received_socket.sendto(data, (ipaddress, portnumber))

            print(ipaddress, portnumber)
            print(response_data)


if __name__ == '__main__':
    argvs = sys.argv[1:]
    main(argvs)
    now = datetime.datetime.now()
