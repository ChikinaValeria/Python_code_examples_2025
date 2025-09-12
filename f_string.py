aloitus = input("Print the selityksen aloitus here: ")
while aloitus == "":
    print("Aloitus can't be empty")
    aloitus = input("Print the selityksen aloitus here: ")
opettaja = input("Print oppettajan nimi here: ")
while opettaja == "":
    print("opettajan nimi can't be empty")
    opettaja = input("Print oppettajan nimi here: ")
k_tyyppi = input("Print kotitehtävän tyyppi here: ")
while k_tyyppi == "":
    print("kotitehtävän tyyppi can't be empty")
    k_tyyppi = input("Print kotitehtävän tyyppi here: ")
l_laji = input("Print lemmikkieläimen laji here: ")
while l_laji == "":
    print("lemmikkieläimen laji can't be empty")
    l_laji = input("Print lemmikkieläimen laji here: ")
l_nimi = input("Print lemmikkieläimen nimi here: ")
while l_nimi == "":
    print("lemmikkieläimen nimi can't be empty")
    l_nimi = input("Print lemmikkieläimen nimi here: ")
l_teko = input("Print lemmikkieläimen teko here: ")
while l_teko == "":
    print("lemmikkieläimen teko can't be empty")
    l_teko = input("Print lemmikkieläimen teko here: ")

print(f'{aloitus}, {opettaja}, en tiedä mihin se {k_tyyppi} oikein joutui! '
      f'Lemmikki{l_laji}ni {l_nimi} afgvarmaankin {l_teko} sen! ')