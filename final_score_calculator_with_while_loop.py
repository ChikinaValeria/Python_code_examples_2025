#while user wants to continue
while True:
    pisteet = 0
    pisteet_count = 0
    # pituus = 0

    #getting pituus value
    while True:
        try:
            pituus = float(input("Anna hypyn pituus: "))
            break
        except ValueError:
            print('Error: Please enter numbers only. Try again.')

    #getting tuomarin pisteet
    while pisteet_count < 5:
        while True:
            try:
                pisteet += float(input(f'Tuomarin {pisteet_count+1} pisteet: '))
                pisteet_count +=1
                #print(pisteet)
                break
            except ValueError:
                print('Error: Please enter numbers only. Try again.')

    #all data collected, processing and printing data
    yhteispisteet = pituus * 0.9 + pisteet
    print(f'Yhteispisteet: {yhteispisteet:.2f}')

    jatka = input("Haluatko aloittaa alusta? y/n ")
    if jatka.lower() != "y":
        break

