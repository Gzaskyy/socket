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


def month_check(data_received):
    month = int(bin(data_received[8][2:].zfill[8]), 2)

    if 12 >= month >= 1:
        return month
    else:
        return 2


def day_check(data_received):
    day = int(bin(data_received[9][2:].zfill[8]), 2)

    if 31 >= day >= 1:
        return day
    else:
        return 2


def hour_check(data_received):
    hour = int(bin(data_received[10][2:].zfill[8]), 2)

    if 23 >= hour >= 0:
        return hour
    else:
        return 2


def minute_check(data_received):
    minute = int(bin(data_received[11][2:].zfill[8]), 2)

    if 59 >= minute >= 0:
        return minute
    else:
        return 2


def total_length_check(data_received):
    total_length = int(bin(data_received[12][2:].zfill[8]), 2)

    if total_length == len(data_received):
        return 1
    else:
        return 2