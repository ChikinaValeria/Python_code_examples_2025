full_name = input('Enter your full name')
name_parts = full_name.split()

initials =''
for part in name_parts:
    initials += part[0].upper() + '. '

print(initials.strip())
