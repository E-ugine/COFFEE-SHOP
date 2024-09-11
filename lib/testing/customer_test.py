import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer
from order import Order


class TestCustomer:
    """Customer in many_to_many.py"""

    def test_has_name(self):
        """Customer is initialized with name"""
        customer = Customer("Mary")
        assert customer.name == "Mary"


    def test_name_length_is_valid(self):
        """name is between 1 and 15 characters"""
        customer = Customer("Mike")
        assert len(customer.name) == 4

       

    def test_has_many_orders(self):
        """customer has many orders"""
        coffee = Coffee("Latte")
        customer_1 = Customer("John")
        customer_2 = Customer("Jane")
        order_1 = Order(customer_1, coffee, 6.0)
        order_2 = Order(customer_1, coffee, 4.0)
        order_3 = Order(customer_2, coffee, 9.0)

    def test_orders_of_type_order(self):
        """customer orders are of type Order"""
        coffee = Coffee("Vanilla")
        customer = Customer("Chris")
        Order(customer, coffee, 7.0)
        Order(customer, coffee, 8.0)

      
    def test_has_many_coffees(self):
        """customer has many coffees"""
        coffee_1 = Coffee("Latte")
        coffee_2 = Coffee("Cappucino")
        coffee_3 = Coffee("Flat White")
        customer = Customer("Agolla")
        Order(customer, coffee_1, 7.0)
        Order(customer, coffee_2, 8.0)

      

   


    
   
        
     
        
        
  