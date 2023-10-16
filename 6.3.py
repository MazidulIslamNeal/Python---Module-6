def convert_gallon_to_liter(gallons):
    liters = gallons * 3.748
    return liters
while True:
    gallons = float(input("Enter the quantity of gasoline in American gallons (entering a negative will quit): "))
    if gallons <0:
        break
    liters = convert_gallon_to_liter(gallons)
    print(f"{gallons:.2f} gallons is equal to {liters:.2f} liters.")
