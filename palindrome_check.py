def is_palindrome(lause):
    letters = []
    for letter in lause:
        if letter.isalpha():
            letters.append(letter.lower())
    reversed_letters = letters[::-1]
    if not reversed_letters:
        raise ValueError("Your phrase should contain at least one letter.")
    return letters == reversed_letters


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
        result = is_palindrome(lause)
        if result:
            print("It is a palindrome.")
        else:
            print("It is NOT a palindrome.")

    except ValueError as e:
        print(e)

    continue_prompt = input("Do you want to start over? (y/n) ")
    if continue_prompt.lower() != "y":
        break
