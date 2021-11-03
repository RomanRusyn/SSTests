import datetime


def sun_angle(time):
    # replace this for solution
    t = time.split(':')
    minutesAfterRise = (int(t[0]) - 6) * 60 + int(t[1])
    degreePerMinute = 180 / (12 * 60)
    if 720 >= minutesAfterRise >= 0:
        return minutesAfterRise * degreePerMinute
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
