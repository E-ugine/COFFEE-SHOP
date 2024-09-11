For this project, You are tasked with building a domain model for a Coffee Shop.

We have three entities: `Coffee`, `Customer`, and `Order`.

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity.

**Note**:  - Before coding, sketch your domain model on paper or a whiteboard:
 - Identify the three main classes: `Customer`, `Coffee`, and `Order`.
 - Establish the relationships between these classes.
   - Determine the attributes and methods that each class will have.
   - Keep in mind the concept of a single source of truth for your data.

## Instructions

To get started, run `pipenv install` while inside of the project directory. Then run
`pipenv shell` to get into the shell.

There are tests to help you check that the code is functional before submitting.
run `pytest` to check all tests.

Run `python debug.py` from the command line to start a `ipdb` session
with your classes defined.Test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.


## Deliverables
### Initializers and Properties

#### Customer

- `Customer __init__(self, name)`
  - Customer is initialized with a name
- `Customer property name`
  - Returns customer's name
  - Names must be of type `str`
  - Names must be between 1 and 15 characters, inclusive
  - Should **be able** to change after the customer is instantiated

#### Coffee

- `Coffee __init__(self, name)`
  - Coffee is initialized with a name
- `Coffee property name`
  - Returns the coffee's name
  - Names must be of type `str`
  - Names length must be greater or equal to 3 characters
  - Should **not be able** to change after the coffee is instantiated
  - _hint: `hasattr()`_

#### Order

- `Order __init__(self, customer, coffee, price)`
  - Order is initialized with a `Customer` instance, a `Coffee` instance, and a
    price
- `Order property price`
  - Returns the price for the order
  - Prices must be of type `float`
  - Price must be a number between 1.0 and 10.0, inclusive
  - Should **not be able** to change after the order is instantiated


### Object Relationship Methods and Properties

#### Order

- `Order property customer`
  - Returns the customer object for that order
  - Must be of type `Customer`
- `Order property coffee`
  - Returns the coffee object for that order
  - Must be of type `Coffee`

#### Coffee

- `Coffee orders()`
  - Returns a list of all orders for that coffee
  - Orders must be of type `Order`
- `Coffee customers()`
  - Returns a **unique** list of all customers who have ordered a particular
    coffee.
  - Customers must be of type `Customer`

#### Customer

- `Customer orders()`
  - Returns a list of all orders for that customer
  - Orders must be of type `Order`
- `Customer coffees()`
  - Returns a **unique** list of all coffees a customer has ordered
  - Coffees must be of type `Coffee`

### Aggregate and Association Methods

#### Customer

- `Customer create_order(coffee, price)`
  - Receives a **coffee object** and a **price number** as arguments
  - Creates and returns a new Order instance and associates it with that
    customer and the coffee object provided.

#### Coffee

- `Coffee num_orders()`
  - Returns the total number of times a coffee has been ordered
  - Returns `0` if the coffee has never been ordered
- `Coffee average_price()`
  - Returns the average price for a coffee based on its orders
  - Returns `0` if the coffee has never been ordered
  - **Reminder**: you can calculate the average by adding up all the orders prices
    and dividing by the number of orders


**Remember**Messy code that works is better than clean code that doesn't.

  