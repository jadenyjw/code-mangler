revenue += self._menu.get_price(order_name)
if(order_name in self._menu.get_menu()):
order_name = order.get_name()
for order in customer.get_orders():
Add a new customer to the restaurant's list
Get the name of the order.
Gets the price of an item inside a menu with the given name.
Given the name of an item, add it to the list of items that the customer ordered.
Initialize a restaurant with its name and its menu. Also give it a blank list of customers.
Initializes a customer
Initializes a menu object.
Initializes an order with the item name.
Returns the menu dictionary of pasta to prices.
Returns the restaurant's revenue of the day based on what all the customers ordered.
Returns this customer's orders
for customer in self._customers:
return revenue
return self._item_name
return self._item_to_prices
return self._item_to_prices[item]
revenue = 0
self._customers = []
self._item_name = name
self._item_to_prices = {"Ravioli": 12.99, "Lasagne": 11.99, "Macaroni": 10.99, "TT2 Spaghetti Code": 29.79}
self._menu = menu
self._name = name
self._orders = []
code_mangler = Customer()
code_mangler.order("Lasagne")
code_mangler.order("Macaroni")
code_mangler.order("Ravioli")
code_mangler.order("TT2 Spaghetti Code")
code_stealer = Customer()
def __init__(self):
def __init__(self):
def __init__(self, name):
def __init__(self, name, menu):
def add_customer(self, customer):
def compute_revenue(self):
def get_menu(self):
def get_name(self):
def get_orders(self):
def get_price(self, item):
def order(self, item):
menu = Menu()
print("The total revenue generated was: " + str(restaurant.compute_revenue()))
restaurant = Restaurant("CSCA08", menu)
restaurant.add_customer(code_mangler)
restaurant.add_customer(code_stealer)
order = Order(item)
return self._orders
self._customers.append(customer)
self._orders.append(order)
class Customer():
class Menu():
class Order():
class Restaurant():
if (__name__ == "__main__"):
