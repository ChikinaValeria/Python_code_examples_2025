def get_input(prompt, error_message):
    """
    Prompts the user for input and repeats the request 
    if the input is empty or consists only of spaces.
    """
    user_input = input(prompt)
    # user_input.strip() возвращает строку, очищенную от пробелов и табов
    # пустая строка считается False
    # not False -> True, пока строка пустая, выполняй
    while not user_input.strip():
        print(error_message)
        user_input = input(prompt)
    return user_input

aloitus = get_input("Print the selityksen aloitus here: ", "Aloitus can't be empty")
opettaja = get_input("Print oppettajan nimi here: ", "opettajan nimi can't be empty")
k_tyyppi = get_input("Print kotitehtävän tyyppi here: ", "kotitehtävän tyyppi can't be empty")
l_laji = get_input("Print lemmikkieläimen laji here: ", "lemmikkieläimen laji can't be empty")
l_nimi = get_input("Print lemmikkieläimen nimi here: ", "lemmikkieläimen nimi can't be empty")
l_teko = get_input("Print lemmikkieläimen teko here: ", "lemmikkieläimen teko can't be empty")

print(f'{aloitus}, {opettaja}, en tiedä mihin se {k_tyyppi} oikein joutui! '
      f'Lemmikki{l_laji}ni {l_nimi} afgvarmaankin {l_teko} sen! ')