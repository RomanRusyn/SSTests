import datetime
import time


def time_converter(time1):
    # replace this for solution
    t = time.strptime(time1, "%H:%M")
    timevalue_12hour = time.strftime("%I:%M %p", t)
    if timevalue_12hour[0]=='0':
        return timevalue_12hour[1:].lower().replace('pm','p.m.').replace('am','a.m.')
    else:
        return timevalue_12hour.lower().replace('pm','p.m.').replace('am','a.m.')


if __name__ == '__main__':
    print("Example:")
    print(time_converter('09:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert time_converter('12:30') == '12:30 p.m.'
    # assert time_converter('09:00') == '9:00 a.m.'
    # assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
