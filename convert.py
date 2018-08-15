def byte_to_int(args):

    length = len(args)

    if length == 1:
        num = int(bin(args)[2:].zfill(8), 2)
        return num
    elif length == 2:
        num = int((bin(args[0][2:].zfill(8) + bin(args[1])[2:].zfill(8))), 2)
        return num

