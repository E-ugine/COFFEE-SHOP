from order import Order

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 3 <= len(value) and not hasattr(self, 'name'):
            self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        all_customers = [order.customer for order in Order.all if order.coffee == self]
        unique_customers = list(set(all_customers))
        return unique_customers

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders) / len(orders) if orders else 0
