initial_string = input('Please, enter the line of numbers without spaces:')
sum = 0
for ch in initial_string:
    sum += int(ch)
print(f'The sum of the numbers is {sum}')