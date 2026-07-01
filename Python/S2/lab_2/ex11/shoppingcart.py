import datetime

cart = [
{"product": "1921213-12", "price": 49.99, "category": "SHIRT"},
{"product": "1224121-12", "price": 59.99, "category": "SHIRT"},
{"product": "3232312-13", "price": 89.99, "category": "SHIRT"},
{"product": "2230020-10", "price": 19.99, "category": "SOCKS"},
{"product": "1224000-49", "price": 95.99, "category": "FRAGRANCE"},
{"product": "3233424-49", "price": 149.99, "category": "SHOES"},
{"product": "2323231-20", "price": 119.99, "category": "SHOES"},
]

whole_price = 0
for i in cart:
    whole_price += i["price"]

sprice = 0
for i in cart:
    if i["category"] == "SHIRT":
        sprice += (i["price"] * 0.6)
    else:
        sprice += i["price"]

cprice = 0
if whole_price > 500:
    cprice = whole_price * 0.9
cart_str = "Cart"

print(f"{cart_str:<34}{datetime.datetime.now().day:02d}.{datetime.datetime.now().month:02d}.{datetime.datetime.now().year:02d} {datetime.datetime.now().hour:02d}:{datetime.datetime.now().minute:02d}")
for i in range(50):
    print("-",end= "")
print("")
for i in cart:
    print(f"{i['category']:<15}{i['product']:<20}{i['price']:>15}")
for i in range(50):
    print("-",end= "")
print("")
pre_price = "Brutto:"
print(f"{pre_price:<30}{whole_price:>20}")
for i in range(50):
    print("-",end= "")
print("")
discount10 = "10% on everything:"
ev = whole_price * 0.1
discountShirts = "40% on shirts:"
print(f"{discount10:<35}{-ev:>15.02f}")
print(f"{discountShirts:<35}{-(whole_price - sprice):>15.02f}")
if cprice > sprice:
    print("The shirts discount is selected!")
    for i in range(50):
        print("-",end= "")
    print("")
    netto = "Netto:"
    print(f"{netto:<35}{sprice:>15.02f}")
    for i in range(50):
        print("-",end= "")
    print("")
else:
    print("The 10% coupon is selected!")
    for i in range(50):
        print("-",end= "")
    print("")
    netto = "Netto:"
    print(f"{netto:<35}{cprice:>15.02f}")
    for i in range(50):
        print("-",end= "")
    print("")