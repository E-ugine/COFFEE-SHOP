from coffee import Coffee
from customer import Customer
#customer 1 & 2 are instances of class Customer
#coffee 1 & 2 are instances of class Coffee
customer1 = Customer("Eugine")
customer2 = Customer("William")
coffee1 = Coffee("Cortado")
coffee2 = Coffee("Cappucino")


customer1.create_order(coffee1, 8.0) #creates an instance of class order. sets customer1 = Eugine, coffee= cortado and price= 8
customer2.create_order(coffee1, 9.0)
customer2.create_order(coffee2, 3.0)
customer2.create_order(coffee2, 6.0)


most_aficionado_for_espresso = Customer.most_aficionado(coffee1) #checks who has spent more on coffee1
print(f"Most aficionado for Espresso: {most_aficionado_for_espresso.name}") 


print(f"Customer: {customer1.name}")
for coffee in customer1.coffees():
    print(f"Ordered Coffee: {coffee.name}")
    print(f"Number of Orders: {coffee.num_orders()}")
    print(f"Average Price: {coffee.average_price()}")
    print(f"Customer: {customer1.name}")
for coffee in customer2.coffees():
    print(f"Ordered Coffee: {coffee.name}")
    print(f"Number of Orders: {coffee.num_orders()}")
    print(f"Average Price: {coffee.average_price()}")