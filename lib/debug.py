from coffee import Coffee
from customer import Customer

c1 = Customer("Alice")
c2 = Customer("Bob")
coffee1 = Coffee("Espresso", 5.0)
coffee2 = Coffee("Latte", 4.5)

# Create orders
c1.create_order(coffee1, 5.0)
c2.create_order(coffee1, 6.0)
c2.create_order(coffee2, 4.5)

# Check who is the most aficionado for Espresso
most_aficionado_for_espresso = Customer.most_aficionado(coffee1)
print(f"Most aficionado for Espresso: {most_aficionado_for_espresso.name}")  # Output: Bob
