while True:
    try:
        annual_mileage = (float(input("Give your estimated annual mileage: ")))
        gasoline_price = (float(input("Give the price of gasoline: ")))
        diesel_price = (float(input("Give the price of diesel: ")))
        gasoline_comsumption = (float(input("Give your estimated gasoline consumption (l/100km): ")))
        diesel_consumption = (float(input("Give your estimated diesel consumption (l/100km): ")))
        diesel_tax = (float(input("Give the diesel fuel tax amount: ")))

        break

    except ValueError:
        print('Error: Please enter numbers only. Try again.')    

gasoline_annual_cost = round(annual_mileage/100 * gasoline_comsumption * gasoline_price, 2)
diesel_annual_cost = round(annual_mileage/100 * diesel_consumption * diesel_price + diesel_tax, 2)
#print(f'gasoline_annual_cost: {gasoline_annual_cost}')
#print(f'diesel_annual_cost: {diesel_annual_cost}')

print(f'The annual travel costs of gasoline-powered car is {gasoline_annual_cost}')
print(f'The annual travel costs of diesel-powered car is {diesel_annual_cost}')

if (gasoline_annual_cost > diesel_annual_cost):
    print(f'The annual travel costs of gasoline-powered car are bigger'
          f' than costs of diesel-powered car by {round(gasoline_annual_cost-diesel_annual_cost, 2)} euros')
elif(gasoline_annual_cost < diesel_annual_cost):
    print(f'The annual travel costs of gasoline-powered car are smaller'
        f' than costs of diesel-powered car by {round(diesel_annual_cost-gasoline_annual_cost, 2)} euros')
else:
    print(f'The annual travel costs for both cars are equal')        
