def unit_price(diam,price):
    r=diam/2
    area = 3.1416*(r**2)
    unit_price = price/area
    return unit_price

price_p1 = float(input("Enter the price of first pizza: "))
diam_p1 = float(input("Enter the diameter of first pizza: "))
ratio1 = unit_price(diam_p1 , price_p1 )

print(f"{ratio1:.2f}")

price_p2 = float(input("Enter the price of second pizza: "))
diam_p2 = float(input("Enter the diameter of second pizza: "))

ratio2 = unit_price(diam_p2 , price_p2 )


if ratio1 < ratio2 :
    print (f"First pizza is reasonable")
elif ratio1 > ratio2 :
    (f"Second pizza is reasonable")
else:
    print (f"both same")
