def is_palindrome(lause):
    letters = []
    for letter in lause:
        if letter.isalpha():
            letters.append(letter.lower())
    print(letters)
    reversed_letters = letters[::-1]
    if len(letters) == 0:
        raise ValueError("Your phrase should contain at least one letter.")
    elif letters == reversed_letters:
        return True
    else:
        return False

candidates = [
    'A man, a plan, a canal: Panama.',
    'Iso rikas sika sökösakissa kirosi.',
    '"Aa, viinaa sitruksilla", kallis kurtisaani ivaa.',
    'Joku satunnainen lause',
    'Madam, I\'m Adam.',
    'Never odd or even.',
    'Was it a car or a cat I saw?',
    'Mr. Owl ate my metal worm.',
    'No lemon, no melon.',
    'Evil rats on no star live.'
]

for c in candidates:
    tulos = 'EI OLE'
    if is_palindrome(c):
        tulos = 'ON'
    print(f'"{c}": {tulos} palindrome')

while True:
    lause = (input('Enter your phrase: '))

    try:
        print(is_palindrome(lause))
    except ValueError as e:
        print(e)

    jatka = input("Haluatko aloittaa alusta? y/n ")
    if jatka.lower() != "y":
        break
