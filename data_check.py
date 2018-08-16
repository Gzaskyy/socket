def requestLen_check(data_received):
    """Checks if the length is a fixed number 6"""
    if len(data_received) == 6:
        return 1
    else:
        return 2


def magicNo_check(data_received):
    """Checks if the magic number equals to 0x497E"""
    if data_received[0] == 0x49 and data_received[1] == 0x7e:
        return 1
    else:
        return 2


def package_type_check(data_received):
    """Checks if the package type equals to 0x0001"""
    if data_received[2] == 0x00 and data_received[3] == 0x01:
        return 1
    else:
        return 2


def request_type_check(data_received):
    """Checks and obtain the time type"""
    if data_received[4] == 0x00 and data_received[5] == 0x01:
        return 1  # Date
    elif data_received[4] == 0x00 and data_received[5] == 0x02:
        return 2  # Time
    else:
        return 3


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
    """check if language is valid and return it"""

    if data_received[4] == 0x00 and data_received[5] == 0x01:
        return 1  # English
    elif data_received[4] == 0x00 and data_received[5] == 0x02:
        return 2  # Te reo Maori
    elif data_received[4] == 0x00 and data_received[5] == 0x03:
        return 3  # German
    else:
        return 4  # Error


def year_check(data_received):
    """check year under 2100 above 0"""

    year = int(bin(data_received[6])[2:].zfill(8) + bin(data_received[7])[2:].zfill(8),2)

    if year >= 0 <= 2100:
        return 1
    else:
        return 2


def month_check(data_received):
    """check month in range 1-12"""
    month = int(bin(data_received[8])[2:].zfill(8), 2)

    if 12 >= month >= 1:
        return 1
    else:
        return 2


def day_check(data_received):
    """check day in range 1-31"""
    day = int(bin(data_received[9])[2:].zfill(8), 2)

    if 31 >= day >= 1:
        return 1
    else:
        return 2


def hour_check(data_received):
    """check hour in range 0-23"""
    hour = int(bin(data_received[10])[2:].zfill(8), 2)

    if 23 >= hour >= 0:
        return 1
    else:
        return 2


def minute_check(data_received):
    """check minute in range 0-59"""
    minute = int(bin(data_received[11])[2:].zfill(8), 2)

    if 59 >= minute >= 0:
        return 1
    else:
        return 2


def total_length_check(data_received):
    """check the text length"""
    total_length = int(bin(data_received[12])[2:].zfill(8), 2)

    if total_length == len(data_received[13:]):
        return 1
    else:
        return 2
