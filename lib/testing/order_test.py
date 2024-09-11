import pytest

from coffee import Coffee
from customer import Customer
from order import Order


class TestOrders:
    '''Order in many_to_many.py'''

    def test_has_price(self):
        '''Order is initialized with a price'''
        coffee = Coffee("Flat White")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 4.0)
        order_2 = Order(customer, coffee, 3.5)

        assert (order_1.price == 4.0)
        assert (order_2.price == 3.5)
    
    def test_price_is_valid(self):
        """price is of type float and between 1.0 and 10.0"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2.0)
        order_2 = Order(customer, coffee, 5.0)
        
        assert isinstance(order_1.price, float)
        assert isinstance(order_2.price, float)
        
     
      