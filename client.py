import socket
import sys


def check_input(argv1, argv2, argv3):

    if argv1 != 'date' or argv1 != 'time':
        return print('Invalid request type!')
    else:
        date_or_time = argv1

    try:
        if argv2 != socket.gethostname():
            return print('Wrong hostname')
    except ValueError:
        print('Unable to retrieve the hostname!')
        exit(1)

    try:
        if int(argv3) >= 64000 or int(argv3) <= 1024:
            return print("Port number must between 1024 and 64000 and according to the port numbers of server, "
                         "please try again")
    except ValueError:
        print('Invalid port number, please try again.')
        exit(1)

    return date_or_time, int(argv2), int(argv3)


def main(data):

    global host_name, port_num
    try:
        date_or_time, host_name, port_num = check_input(data[0], data[1], data[2])
    except TypeError:
        print('Invalid input!')
        exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host_name, 5010))

    message = "hello world"
    message_encode = message.encode('utf-8')

    sock.sendto(message_encode, (host_name, port_num))


if __name__ == '__main__':
    argvs = sys.argv[1:]
    main(argvs)
