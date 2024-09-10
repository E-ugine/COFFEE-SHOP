from order import Order
from coffee import Coffee

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        self.orders = []
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        non_unique = [order.coffee for order in Order.all if order.customer == self]
        unique = set(non_unique)
        return list(unique)

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def total_spent(cls, customer, coffee):
        # Calculate total amount spent by the customer on the specific coffee
        return sum(order.price for order in Order.all if order.customer == customer and order.coffee == coffee)

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise Exception("Invalid coffee object provided")

        # List of customers who have ordered the specific coffee
        customers_for_coffee = [order.customer for order in Order.all if order.coffee == coffee]

        # Return None if no customers ordered the coffee
        if not customers_for_coffee:
            return None

        # Find the customer who has spent the most money on the coffee
        return max(customers_for_coffee, key=lambda customer: cls.total_spent(customer, coffee))
