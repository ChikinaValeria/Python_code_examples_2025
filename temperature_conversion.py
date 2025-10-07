def convert_temperature(degrees, from, to):
    if from == 'c':
        if to == 'f':
            return degrees*9/5+32
        if to == 'k':
            return degrees + 273
    elif from == 'f':
        if to == 'c':
            return (degrees - 32)*5/9
        if to == 'k':
            return (degrees - 32)*5/9 + 273
    elif from == 'k':
        if to == 'c':
            return degrees - 273
        if to == 'f':
            return (degrees - 273)*9/5+32
    else:
        print('Invalid input')
        

