on_pizza = []

while True:
    print("\nType 'Quit' to stop.")
    toppings = input("Add toppings: ")
    toppings = toppings.capitalize()

    if toppings != "Quit":
        on_pizza.append(toppings)        
        for i in on_pizza:
            print(f"{i} has been added to the pizza.")
    else:
        break