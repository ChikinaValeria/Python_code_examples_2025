class Pizza:
    def __init__(self, nimi, taytteet):
        self.nimi = nimi
        self.taytteet = [t for t in taytteet if t is not None]
        self.hinnat = {'normaali': None, 'perhe': None, 'pannu': None}


    def hae_taytteet(self):
        if not self.taytteet:
            return 'Pizzalla ei ole mitään.'

        return ", ".join(self.taytteet)

    def onko_tayte(self, t):
        return t in self.taytteet

    def aseta_hinnat(self, normaali_hinta, perhe_hinta, pannu_hinta):
        self.hinnat['normaali'] = float(normaali_hinta)
        self.hinnat['perhe'] = float(perhe_hinta)
        self.hinnat['pannu'] = float(pannu_hinta)

    def hae_hinnat(self):
        return (self.hinnat['normaali'], self.hinnat['perhe'], self.hinnat['pannu'])

pizzat = {
1: Pizza('Bolognese', ['jauheliha']),
2: Pizza('Frutti di Mare', ['ananas', 'katkarapu', 'tonnikala']),
3: Pizza('Americano', ['ananas', 'aurajuusto', 'kinkku']),
4: Pizza('Opera Special', ['kinkku', 'salami', 'tonnikala']),
5: Pizza('Mexicana', ['ananas', 'pepperoni', 'chili', 'tacokastike']),
6: Pizza('Julia', ['ananas', 'aurajuusto', 'katkarapu', 'kinkku']),
7: Pizza('Empire Special', ['katkarapu', 'kinkku', 'mustapippuri',
                             'salami', 'sipuli', 'tuplajuusto',
                             'valkosipuli']),
8: Pizza('Kummisetä', ['herkkusieni', 'katkarapu', 'kinkku',
                       'valkosipuli']),
9: Pizza('Chicken Hawaii', ['ananas', 'aurajuusto', 'kana']),
11: Pizza('Romeo', ['ananas', 'aurajuusto', 'katkarapu', 'salami']),
12: Pizza('Vegetariana', ['herkkusieni', 'oliivi', 'paprika',
                          'sipuli', 'tomaatti']),
13: Pizza('Dillinger', ['jauheliha', 'kinkku', 'salami', 'sipuli']),
14: Pizza('Papa\'s Special', ['aurajuusto', 'mustapippuri', 'oliivi',
                              'paprika', 'salami', 'sipuli']),
15: Pizza('Quattro Stagioni', ['herkkusieni', 'katkarapu', 'kinkku',
                               'paprika']),
16: Pizza('Cambretti', ['tuplajuusto', 'katkarapu', 'valkosipuli']),
17: Pizza('Pepperoni', ['paprika', 'pepperoni', 'tonnikala']),
19: Pizza('Spicy Hot Crispy', ['mausteinen naudanliha', 'sipuli',
                               'tomaatti', 'chili']),
21: Pizza('Finlandia', ['kana', 'katkarapu', 'kinkku',
                        'salami', 'tonnikala']),
23: Pizza('Driver\'s Special', ['pekoni', 'pepperoni', 'kinkku',
                                'salami', 'aurajuusto']),
26: Pizza('Fantasia', [None, None, None, None])
}

pizzat[1].aseta_hinnat(11.50, 19.50, 16.50)
pizzat[2].aseta_hinnat(10.00, 17.00, 14.00)
pizzat[3].aseta_hinnat(13.00, 21.00, 18.00)
pizzat[4].aseta_hinnat(11.50, 19.50, 16.50)
pizzat[5].aseta_hinnat(13.00, 21.00, 18.00)
pizzat[6].aseta_hinnat(14.50, 23.00, 20.00)
pizzat[7].aseta_hinnat(11.50, 19.50, 16.50)
pizzat[8].aseta_hinnat(13.00, 21.00, 18.00)
pizzat[9].aseta_hinnat(13.00, 21.00, 18.00)
pizzat[11].aseta_hinnat(14.50, 23.00, 20.00)
pizzat[12].aseta_hinnat(11.50, 19.50, 16.50)
pizzat[13].aseta_hinnat(10.00, 17.00, 14.00)
pizzat[14].aseta_hinnat(11.50, 19.50, 16.50)
pizzat[15].aseta_hinnat(14.50, 23.00, 20.00)
pizzat[16].aseta_hinnat(13.00, 21.00, 18.00)
pizzat[17].aseta_hinnat(11.50, 19.50, 16.50)
pizzat[19].aseta_hinnat(11.50, 19.50, 16.50)
pizzat[21].aseta_hinnat(11.50, 19.50, 16.50)
pizzat[23].aseta_hinnat(13.00, 21.00, 18.00)
pizzat[26].aseta_hinnat(11.50, 19.50, 16.50)

header = "{:^3} {:<24} {:^9} {:^7} {:^7}".format(
    "Nro", "Nimi", "Normaali", "Perhe", "Pannu"
)

print(header)
print(" " * 3 + "-" * (len(header) - 3))

for nro in sorted(pizzat.keys()):
    pizza = pizzat[nro]

    normaali_hinta, perhe_hinta, pannu_hinta = pizza.hae_hinnat()

    hinnat_str = "{:.2f} {:8.2f} {:8.2f}".format(
        normaali_hinta, perhe_hinta, pannu_hinta
    )

    print("{:>3} {:<24} {}".format(nro, pizza.nimi, hinnat_str))

    print(" " * 4 + pizza.hae_taytteet())
    print()