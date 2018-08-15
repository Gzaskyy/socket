import sys


def get_ports():
    print("test")
    argv1 = "sdfsd"
    try:
        port_eng = int(argv1)
        print(port_eng)
        if port_eng >= 64000 or port_eng <= 1024:
            return "Port number must between 1024 and 64000, please try again"
        else:
            return port_eng
    except ValueError:
        print("Not a valid port number, please try again.")


if __name__ == '__main__':
    argvs = sys.argv[1:]
    get_ports()

    # print(argvs[0])
