
pizza_orders = ["Margherita", "Pepperoni", "BBQ Honey Chicken", "Meat Lovers", "Hawaiian"]

finished_pizzas = []

while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    finished_pizzas.append(current_pizza)
    print(f"The pizza {current_pizza} was made. Preparing to dispense in box.")

for pizza in finished_pizzas:
    print(f"Your {pizza} pizza is finished! Please come pick it up!")
