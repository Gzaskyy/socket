import datetime


def byte_to_int(args):
    """convert byte data into int"""
    length = len(args)

    if length == 1:
        num = int((bin(args[0])[2:].zfill(8)), 2)
        return num
    elif length == 2:
        num = int((bin(args[0])[2:].zfill(8) + bin(args[1])[2:].zfill(8)), 2)
        return num


def int_to_2byte(args):
    """convert int into 2 bytes"""

    byte_year = int((bin(args)[2:].zfill(16)), 2).to_bytes(2, 'big')

    return byte_year


def int_to_1byte(args):
    """convert any int to 1 byte"""

    byte_num = int((bin(args)[2:].zfill(8)), 2).to_bytes(1, 'big')

    return byte_num


