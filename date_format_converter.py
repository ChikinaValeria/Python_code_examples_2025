months = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

date_string = input("Enter a date in dd/mm/yyyy format: ")

day, month, year = date_string.split('/')

month_index = int(month) - 1
month_text = months[month_index]

print(f'{day} of {month_text} {year} y.')
