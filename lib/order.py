from customer import Customer
from coffee import Coffee
class Order(Customer,Coffee):
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        #from customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("Customer must be an instance of Customer.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        #from coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise ValueError("Coffee must be an instance of Coffee.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
