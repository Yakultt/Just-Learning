pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],

}

print(f"you ordered a {pizza['crust']}-crust pizza ")
print(f"here are your toppings!")

for topping in pizza["toppings"]:
    print(f"\t{topping}")