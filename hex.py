import os
import time


def type_phone(characters: list, cord=[], delay=0.1):

    try:
        # If coordinates aren't defined it'll send an enter
        # otherwise it'll send a click in the specified
        # coordinates
        if not cord:
            command = 'adb shell input keyevent 66'
        else:
            x, y = cord
            command = f'adb shell input tap {x} {y}'

        for character in characters:
            time.sleep(delay)
            os.system(f'adb shell input text "{character}"')
            time.sleep(delay)
            os.system(command)
            time.sleep(delay)
    except KeyboardInterrupt:
        print('\n')
    except Exception as err:
        print(err)


def click(x, y):
    os.system(f'adb shell input tap {x} {y}')
    print('ok')


if __name__ == '__main__':
    hex_values = []
    for n in range(16, 257):
        # hex_values.append(hex(n)[2:].upper())
        hex_values.append(f'{n:X}')

    # Do a click on 400, 650 x/y coordinates of phone
    # Make sure that the phone keyboard is open
    click(400, 1600)
    # Enter (if the keyboard is already opened it'll just
    # send a letter, that doesn't matter in my situation)
    os.system('adb shell input keyevent 66')

    type_phone(hex_values)
