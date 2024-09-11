class Customer:
    all = [] #stores all customer instances

    def __init__(self, name): #initializes a new customer
        self.name = name
        type(self).all.append(self)

    @property #this decorator will help get _name
    def name(self):
        return self._name

#the setter method will check if name is a str and of length between 1 and 15,inclusive.
#if true, it then assigns the private _name attribute less it will raise an error
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

#this method will return all orders that belong to the customer instance(self)
#checks whether the current attributes matches the current customer
    def orders(self):
        from order import Order #order class is imported here to avoid circular import errors.
        return [order for order in Order.all if order.customer is self]

#this method will return list of types of coffees that the current customer has ordered.
#REMEMBER sets don't allow duplicates. To ensure each coffee type only appears once we use the set comprehension.
#the set is converted to list

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, new_coffee, new_price):
        from order import Order
        return Order(self, new_coffee, new_price)

#the @class method will find the customer who has spent the most money on a specific coffee.
#cls.all  is the list of all Customer instances.
#the method filters Order.all to get all orders for the given coffee (coffee_all_orders). 
# It then uses max() to find the customer in cls.all (the list of all customers) who has spent the most on that coffee by summing the prices of their orders.
#  If no orders are found for the given coffee, it returns None
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        if coffee_all_orders := [order for order in Order.all if order.coffee is coffee]:
            return max(cls.all, key=lambda customer: sum( order.price  for order in coffee_all_orders if order.customer is customer ),)
        
        return None
                       
                
                
                
                   
                   
                    
               
            
       
