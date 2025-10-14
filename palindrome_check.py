
def on_palindromi(sana):
    takaperi = ''.join(list(reversed(sana)))
    return sana == takaperi

def palindrome_check(lause):
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
    'Joku satunnainen lause'
]

for c in candidates:
    tulos = 'EI OLE'
    if on_palindromi(e):
        tulos = 'ON'
    print(f'"{e}": {tulos} palindromi')

while True:
    lause = (input('Enter your phrase: '))

    try:
        print(palindrome_check(lause))
    except ValueError as e:
        print(e)

    jatka = input("Haluatko aloittaa alusta? y/n ")
    if jatka.lower() != "y":
        break
