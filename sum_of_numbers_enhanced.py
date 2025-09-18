initial_string = input('Please, enter the line of numbers without spaces:')
sum = sum(int(digit) for digit in initial_string)
print(f'The sum of the numbers is {sum}')