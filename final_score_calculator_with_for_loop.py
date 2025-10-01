while True:
    pisteet = 0
    pituus = 0
    try:
        pituus = float(input("Anna hypyn pituus: "))

        for i in range(5):
            pisteet += float(input(f'Tuomarin {i+1} pisteet: '))

        print(pisteet)
        yhteispisteet = pituus * 0.9 + pisteet
        print(f'Yhteispisteet: {yhteispisteet:.2f}')

        jatka = input("Haluatko aloittaa alusta? y/n ")
        if jatka.lower() != "y":
            break

    except ValueError:
        print('Error: Please enter numbers only. Try again.')

