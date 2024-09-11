import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer
from order import Order


class TestCoffee:
    """Coffee in many_to_many.py"""

    def test_has_name(self):
        """Coffee is initialized with a name"""
        coffee = Coffee("Cappucino")
        assert coffee.name == "Cappucino"

    def test_name_is_valid_string(self):
        """Coffee is initialized with a name of type str longer than 2.0 chars"""
        coffee = Coffee("Cappucino")
        assert isinstance(coffee.name, str)

    def test_has_many_orders(self):
        """coffee has many orders"""
        coffee_1 = Coffee("Hazelnut")
        coffee_2 = Coffee("Mocha")
        customer = Customer("Wayne")
        order_1 = Order(customer, coffee_1, 2.0)
        order_2 = Order(customer, coffee_1, 5.0)
        order_3 = Order(customer, coffee_2, 5.0)

      

    