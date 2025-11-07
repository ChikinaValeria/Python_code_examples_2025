class Pelaaja:
    def __init__(self, nimi, pisteet=0, esineet=[]):
        self.nimi = nimi
        self.pisteet = pisteet
        self.esineet = list(esineet)

    def ota_esine(self, esine):
        """Lisää esineen pelaajan inventaarioon"""
        if not esine in self.esineet:
            self.esineet.append(esine)
        else:
            print(f'{esine} on joo mukana! ei lisätty!')

    def pudota_esine(self, esine):
        if esine in self.esineet:
            self.esineet.remove(esine)
            return True
        return False

    def tulosta_esineet(self):
        if self.esineet:
            print('Sinulla on mukanasi:')
            for esine in self.esineet:
                print(f'- {esine}')
        else:
            print('Sinulla ei ole mitään.')
        print()

e = Pelaaja('Espe', 22, ['piano', 'rumpu', 'kukka'])
print(f'Tervetuloa peliin, {e.nimi}. Sinulla on {e.pisteet} pistettä.')
e.tulosta_esineet()