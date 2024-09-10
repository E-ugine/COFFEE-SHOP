from customer import Customer
from coffee import Coffee
from order import Order

# Create some instances
customer1 = Customer("Alice")
coffee1 = Coffee("Latte", 5.0)

# Create an order
order1 = customer1.create_order(coffee1, 5.0)

# Check customer orders
print(customer1.orders())

# Check coffee orders
print(coffee1.orders())

# Get the average price of the coffee
print(coffee1.average_price())
