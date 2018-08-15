def requestLen_check(data_received):
    if len(data_received) == 6:
        return 1
    else:
        return 2


def magicNo_check(data_received):
    if data_received[0] == 0x49 and data_received[1] == 0x7e:
        return 1
    else:
        return 2


def package_type_check(data_received):
    if data_received[2] == 0x00 and data_received[3] == 0x01:
        return 1
    else:
        return 2


def request_type_check(data_received):
    if data_received[4] == 0x00 and data_received[5] == 0x01:
        return 1
    else:
        return 2


def responseLen_check(data_received):
    if len(data_received) >= 13:
        return 1
    else:
        return 2


def response_pacType_check(data_received):
    if data_received[2] == 0x00 and data_received[3] == 0x02:
        return 1
    else:
        return 2


def language_check(data_received):
    """4-5"""

    if data_received[4] == 0x00 and data_received[5] == 0x01:
        return 1  # English
    elif data_received[4] == 0x00 and data_received[5] == 0x02:
        return 2  # Te reo Maori
    elif data_received[4] == 0x00 and data_received[5] == 0x03:
        return 3  # German
    else:
        return 4  # Error


def year_check(data_received):
    year = int((bin(data_received[6][2:].zfill[8]) + bin(data_received[7][2:].zfill[8])), 2)

    if year <= 2100:
        return year
    else:
        return 2
