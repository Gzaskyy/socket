import socket
import select
import sys
from data_check import *


def check_input(argv1, argv2, argv3):
    """
       Check the user input if all valid.
       Returns 3 parameters which stand for requested data type,
       hostname of server, port number of server.
    """
    if argv1 != 'date' and argv1 != 'time':  # Request type check
        print("Invalid request type!")
        exit(1)

    try:
        if int(argv3) >= 64000 or int(argv3) <= 1024:  # port number check
            return print("Port number must between 1024 and 64000 and according to the port numbers of server, "
                         "please try again")
    except TypeError:
        print("Invalid port number, please try again.")
        exit(1)

    return argv1, argv2, argv3


def main(data):
    """
       The main client function
       Initialize the whole client terminal
       Send packet to server terminal
       Receive response data from server terminal
    """
    global host_name, port_num, date_or_time
    try:
        date_or_time, host_name, port_num = check_input(data[0], data[1], data[2])
    except ValueError:
        print("Invalid input!")
        exit(1)

    'Check if a valid hostname'
    try:
        socket.getaddrinfo(host_name, int(port_num))
    except socket.gaierror:
        print("Unable to parse the address!")
        exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = bytearray()  # Which will be sent to server terminal
    message.append(0x49)   # Add Magic number
    message.append(0x7E)
    message.append(0x00)   # Add PacketType
    message.append(0x01)

    if date_or_time == 'date':    # Add request type - date
        message.append(0x00)
        message.append(0x01)
    elif date_or_time == 'time':  # Add request type - time
        message.append(0x00)
        message.append(0x02)

    sock.sendto(message, (host_name, int(port_num)))

    received_data = [sock]
    timeout = 1

    rd, wd, ex = select.select(received_data, [], [], timeout)

    while 1:  # Infinite loop for receive the packet form server terminal

        for received_socket in rd:

            data, address = received_socket.recvfrom(1024)  # Receive data,

            "Check if received data meets the standard"
            if responseLen_check(data) == 1:
                if magicNo_check(data) == 1:
                    print("Magic Number is: ", hex(int(("{0}{1}".format(bin(data[0])[2:].zfill(8),
                                                                        bin(data[1])[2:].zfill(8))), 2)))
                    if response_pacType_check(data) == 1:
                        print("Packet Type is: ", int(("{0}{1}".format(bin(data[2])[2:].zfill(8),
                                                                       bin(data[3])[2:].zfill(8))), 2))
                        if language_check(data) == 1 or \
                                language_check(data) == 2 or language_check(data) == 3:
                            print("Language code is: ",
                                  int(("{0}{1}".format(bin(data[4])[2:].zfill(8),
                                                       bin(data[5])[2:].zfill(8))), 2))
                            if year_check(data) == 1:
                                print("year is: ",
                                      int(("{0}{1}".format(bin(data[6])[2:].zfill(8),
                                                           bin(data[7])[2:].zfill(8))), 2))
                                if month_check(data) == 1:
                                    print("Month is: ", int(bin(data[8])[2:].zfill(8), 2))
                                    if day_check(data) == 1:
                                        print("Day is: ", int(bin(data[9])[2:].zfill(8), 2))
                                        if hour_check(data) == 1:
                                            print("Hour is: ", int(bin(data[10])[2:].zfill(8), 2))
                                            if minute_check(data) == 1:
                                                print("Minute is: ", int(bin(data[11])[2:].zfill(8), 2))
                                                if total_length_check(data) == 1:
                                                    print("Text length is: ", int(bin(data[12])[2:].zfill(8), 2))
                                                    print(data[13:].decode())
                                                else:
                                                    print("text length check failed")
                                                    exit(1)
                                            else:
                                                print("Minute check failed")
                                                exit(1)
                                        else:
                                            print("Hour check failed")
                                            exit(1)
                                    else:
                                        print("Day check failed")
                                        exit(1)
                                else:
                                    print("Month check failed")
                                    exit(1)
                            else:
                                print("Year check failed")
                                exit(1)
                        else:
                            print("language check failed")
                            exit(1)
                    else:
                        print("PacketType check failed")
                        exit(1)
                else:
                    print("Magic number check failed")
                    exit(1)
            else:
                print("Response packet length check failed")
                exit(1)


if __name__ == '__main__':
    argvs = sys.argv[1:]
    main(argvs)
