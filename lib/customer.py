class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        from order import Order
        non_unique = [order.coffee for order in Order.all if order.customer == self]
        unique = set(non_unique)
        return list(unique)

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def total_spent(cls, customer, coffee):
        from order import Order
        return sum(order.price for order in Order.all if order.customer == customer and order.coffee == coffee)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise Exception("Invalid coffee object provided")

        customers_for_coffee = [order.customer for order in Order.all if order.coffee == coffee]

        if not customers_for_coffee:
            return None

        return max(customers_for_coffee, key=lambda customer: cls.total_spent(customer, coffee))
