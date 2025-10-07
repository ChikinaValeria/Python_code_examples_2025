import sys

SYSTEM_NAMES = {
    'c': 'Celcius',
    'f': 'Fahrenheit',
    'k': 'Kelvin'
}

def convert_temperature(degrees, sys_from, sys_to):
    if sys_from == sys_to:
        raise ValueError ('Invalid input. Systems should be different.')
    elif sys_from not in ['c', 'f', 'k'] or sys_to not in ['c', 'f', 'k']:
        raise ValueError ('Invalid input. Input should be "c", "f" or "k".')
    elif sys_from == 'c':
        if sys_to == 'f':
            return degrees*9/5+32
        if sys_to == 'k':
            return degrees + 273
    elif sys_from == 'f':
        if sys_to == 'c':
            return (degrees - 32)*5/9
        if sys_to == 'k':
            return (degrees - 32)*5/9 + 273
    elif sys_from == 'k':
        if sys_to == 'c':
            return degrees - 273
        if sys_to == 'f':
            return (degrees - 273)*9/5+32

while True:
    try:
        degrees = float(input('Enter degrees: '))


    except ValueError:
        print('Invalid input. Degrees should be numeric.')
        sys.exit()

    sys_from = input('From which system to convert? Type "c" for Celsius, "f" for Fahrenheit and "k" for Kelvin: ').lower()
    sys_to = input('To which system to convert? Type "c" for Celsius, "f" for Fahrenheit and "k" for Kelvin: ').lower()

    try:
        temperature = convert_temperature(degrees, sys_from, sys_to)

        if type(temperature) == float:
            from_name = SYSTEM_NAMES.get(sys_from.lower())
            to_name = SYSTEM_NAMES.get(sys_to.lower())
            print(f'{degrees} {from_name} equals {temperature:.1f} {to_name}')
        else:
            print(temperature)
    except ValueError as e:
        print(e)

    jatka = input("Haluatko aloittaa alusta? y/n ")
    if jatka.lower() != "y":
        break
