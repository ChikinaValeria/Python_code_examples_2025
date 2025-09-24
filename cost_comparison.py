ANNUAL_MILEAGE = (float(input("Give your estimated annual mileage: ")))
GASOLINE_PRICE = (float(input("Give the price of gasoline: ")))
DIESEL_PRICE = (float(input("Give the price of diesel: ")))
GASOLINE_CONSUMPTION = (float(input("Give your estimated gasoline consumption (l/100km): ")))
DIESEL_CONSUMPTION = (float(input("Give your estimated diesel consumption (l/100km): ")))
DIESEL_TAX = (float(input("Give the diesel fuel tax amount: ")))

gasoline_annual_cost = round(ANNUAL_MILEAGE/100 * GASOLINE_CONSUMPTION * GASOLINE_PRICE, 2)
diesel_annual_cost = round(ANNUAL_MILEAGE/100 * DIESEL_CONSUMPTION * DIESEL_PRICE + DIESEL_TAX, 2)
print(f'gasoline_annual_cost: {gasoline_annual_cost}')
print(f'diesel_annual_cost: {diesel_annual_cost}')

print(f'The annual travel costs of gasoline-powered car is {gasoline_annual_cost}')
print(f'The annual travel costs of diesel-powered car is {diesel_annual_cost}')

if (gasoline_annual_cost > diesel_annual_cost):
    print(f'The annual travel costs of gasoline-powered car are bigger than costs of diesel-powered car by {gasoline_annual_cost-diesel_annual_cost} euros')
elif(gasoline_annual_cost < diesel_annual_cost):
    print(f'The annual travel costs of gasoline-powered car are smaller than costs of diesel-powered car by {diesel_annual_cost-gasoline_annual_cost} euros')
else:
    print(f'The annual travel costs of gasoline-powered car are equal to ones of diesel-powered car')        
