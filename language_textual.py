import datetime

now = datetime.datetime.now()

"""Month dictionary"""
month_english = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
                 12: 'December'}

month_german = {1: 'Januar', 2: 'Februar', 3: 'M̈arz', 4: 'April', 5: 'Mai', 6: 'Juni',
                7: 'Juli', 8: 'August', 9: 'September', 10: 'Oktober', 11: ' November',
                12: 'Dezember'}

month_mori = {1: 'Kohitatea', 2: 'Huitanguru', 3: 'Poututerangi',
              4: 'Paengawhawha', 5: 'Haratua', 6: 'Pipiri', 7: 'Hongongoi',
              8: 'Hereturikoka', 9: 'Mahuru', 10: 'Whiringaanuku',
              11: 'Whiringaarangi', 12: 'Hakihea'}


if __name__ == '__main__':
    now = datetime.datetime.now()


def to_english_date():
    return ("Today's date is " + month_english[now.month] + " " + str(now.day) + ", " + str(now.year)).encode("utf-8")


def to_english_time():
    return ("The current time is " + str(now.hour) + ":" + str(now.minute)).encode("utf-8")


def to_mori_date():
    return ("Ko te ra o tenei ra ko " + month_mori[now.month] + " " + str(now.day) + ", " + str(now.year)).encode(
        "utf-8")


def to_mori_time():
    return ("Ko te wa o tenei wa " + str(now.hour) + ":" + str(now.minute)).encode("utf-8")


def to_german_date():
    return ("Heute ist der " + month_german[now.month] + " " + str(now.day) + ". " + str(now.year)).encode("utf-8")


def to_german_time():
    return ("Die Uhrzeit ist " + str(now.hour) + ":" + str(now.minute)).encode("utf-8")
