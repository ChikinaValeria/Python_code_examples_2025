pizzat = {
    1: {'nimi': 'Bolognese',
        'taytteet': ['jauheliha'], 'hinta': 2},
    2: {'nimi': 'Frutti di Mare',
        'taytteet': ['ananas', 'katkarapu', 'tonnikala'], 'hinta': 1},
    3: {'nimi': 'Americano',
        'taytteet': ['ananas', 'aurajuusto', 'kinkku'], 'hinta': 3},
    4: {'nimi': 'Opera Special',
        'taytteet': ['kinkku', 'salami', 'tonnikala'], 'hinta': 2},
    5: {'nimi': 'Mexicana',
        'taytteet': ['ananas', 'pepperoni', 'chili',
                     'tacokastike'], 'hinta': 3},
    6: {'nimi': 'Julia',
        'taytteet': ['ananas', 'aurajuusto', 'katkarapu',
                     'kinkku'], 'hinta': 4},
    7: {'nimi': 'Empire Special',
        'taytteet': ['katkarapu', 'kinkku', 'mustapippuri',
                     'salami', 'sipuli', 'tuplajuusto',
                     'valkosipuli'], 'hinta': 2},
    8: {'nimi': 'Kummisetä',
        'taytteet': ['herkkusieni', 'katkarapu', 'kinkku',
                     'valkosipuli'], 'hinta': 3},
    9: {'nimi': 'Chicken Hawaii',
        'taytteet': ['ananas', 'aurajuusto', 'kana'], 'hinta': 3},
    11: {'nimi': 'Romeo',
         'taytteet': ['ananas', 'aurajuusto', 'katkarapu',
                      'salami'], 'hinta': 4},
    12: {'nimi': 'Vegetariana',
         'taytteet': ['herkkusieni', 'oliivi', 'paprika',
                      'sipuli', 'tomaatti'], 'hinta': 2},
    13: {'nimi': 'Dillinger',
         'taytteet': ['jauheliha', 'kinkku', 'salami',
                      'sipuli'], 'hinta': 1},
    14: {'nimi': 'Papa''s Special',
         'taytteet': ['aurajuusto', 'mustapippuri', 'oliivi',
                      'paprika', 'salami', 'sipuli'], 'hinta': 2},
    15: {'nimi': 'Quattro Stagioni',
         'taytteet': ['herkkusieni', 'katkarapu', 'kinkku',
                      'paprika'], 'hinta': 4},
    16: {'nimi': 'Cambretti',
         'taytteet': ['tuplajuusto', 'katkarapu',
                      'valkosipuli'], 'hinta': 3},
    17: {'nimi': 'Pepperoni',
         'taytteet': ['paprika', 'pepperoni', 'tonnikala'], 'hinta': 2},
    19: {'nimi': 'Spicy Hot Crispy',
         'taytteet': ['mausteinen naudanliha', 'sipuli',
                      'tomaatti', 'chili'], 'hinta': 1},
    21: {'nimi': 'Finlandia',
         'taytteet': ['kana', 'katkarapu', 'kinkku',
                      'salami', 'tonnikala'], 'hinta': 2},
    23: {'nimi': 'Driver''s Special',
         'taytteet': ['pekoni', 'pepperoni', 'kinkku',
                      'salami', 'aurajuusto'],'hinta': 3},
    26: {'nimi': 'Fantasia',
         'taytteet': [None, None, None, None], 'hinta': 1}
}

pizzanumerot = sorted(list(pizzat.keys()))
print("Tervetuloa Guido’s Pizza Palaceen, mitä haluaisitte?")
summa = 0
while True:
    try:
        numero = int(input('Anna pizzan numero(0 = lopetus): '))
        if numero in pizzanumerot:
            nimi = pizzat[numero]['nimi']
            while True:
                try:
                    kappalemäärä = int(input(f'Pizzan {nimi} kappalemäärä: '))
                    if 0 < kappalemäärä <= 50:
                        print(f'Välisumma: {kappalemäärä} x {pizzat[numero]['hinta']} = {kappalemäärä * pizzat[numero]['hinta']} euroa')
                        summa += kappalemäärä * pizzat[numero]['hinta']
                        #print(summa)
                        break
                    else:
                        print("Saat tilata yhdestä 50 palaan kutakin pizzaa!")
                except ValueError:
                    print("Anna kappalemäärä kokonaislukuna!")
        elif numero == 0:
            break
        else:
            print(f'Pahoittelut, pizzaa numero {numero} ei ole listalla.')
    except ValueError:
        print("Anna pizzan numero kokonaislukuna!")
print(summa)
print(f'Kiitos tilauksestanne! Kokonaishintanne on {summa} euroa.')


