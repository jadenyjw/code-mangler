class Menu():
	"A class that represents the restaurant's menu"
	def __init__(self):
		'''(Menu) -> NoneType
		Initializes a menu object.
		'''
		# Initialize a menu with pasta items to prices.
		self._item_to_prices = {"Ravioli": 12.99, "Lasagne": 11.99, "Macaroni": 10.99, "TT2 Spaghetti Code": 29.79}

	def get_price(self, item):
		'''(Menu, str) -> float
		Gets the price of an item inside a menu with the given name.
		'''
		return self._item_to_prices[item]


	def get_menu(self):
		'''(Menu) -> dict {str:int}
		Returns the menu dictionary of pasta to prices.
		'''
		return self._item_to_prices



class Restaurant():
	"Class representing a restaurant."

	def __init__(self, name, menu):
		'''(Restaurant, str, Menu) -> NoneType
		Initialize a restaurant with its name and its menu. Also give it a blank list of customers.
		'''
		# Initialize the name of the restaurant.
		self._name = name
		# Initialize a list of customers.
		self._customers = []
		# Set current restaurant's menu to passed in menu.
		self._menu = menu

	def add_customer(self, customer):
		'''(Restaurant, Customer) -> NoneType
		Add a new customer to the restaurant's list
		'''
  		self._customers.append(customer)

	def compute_revenue(self):
		'''(Restaurant) -> float
		Returns the restaurant's revenue of the day based on what all the customers ordered.
		'''
		revenue = 0
		# Loop through all the customers of the day
		for customer in self._customers:
			# and their their orders.
			for order in customer.get_orders():
				# If the order's name is indeed part of the menu, then add that item's price to the revenue variable
				order_name = order.get_name()
				if(order_name in self._menu.get_menu()):
					# Add to the current generated revenue.
					revenue += self._menu.get_price(order_name)

		return revenue

class Customer():
	"Class representing customers of the restaurant"

	def __init__(self):
		'''(Customer) -> NoneType
		Initializes a customer
		'''
		# Make an empty list of orders for the customer
		self._orders = []

	def order(self, item):
		'''(Customer, str) -> NoneType
		Given the name of an item, add it to the list of items that the customer ordered.
		'''
			# Make an Order item based on the given name
  		order = Order(item)
  		# Add this item to the customer's ordered list
  		self._orders.append(order)

	def get_orders(self):
		'''(Customer) -> list of Orders
		Returns this customer's orders
		'''
  		return self._orders


class Order():
	"Class representing an item a customer ordered."
	def __init__(self, name):
		'''(Order, str) -> NoneType
		Initializes an order with the item name.
		'''
		# Set the item's name.
		self._item_name = name

	def get_name(self):
		'''(Order) -> str
		Get the name of the order.
		'''
		return self._item_name



if (__name__ == "__main__"):

	# Create a new menu.
	menu = Menu()

	restaurant = Restaurant("CSCA08", menu)
	# Create a customer.
	code_mangler = Customer()
	# Add the customer to the restaurant.
	restaurant.add_customer(code_mangler)
	# Customer orders some items.
	code_mangler.order("Ravioli")
	code_mangler.order("Macaroni")
	# Create another customer, who orders more items.
	code_stealer = Customer()
	restaurant.add_customer(code_stealer)
	code_mangler.order("Lasagne")
	code_mangler.order("TT2 Spaghetti Code")
	# Get the total amount of revenue generated.
	print("The total revenue generated was: " + str(restaurant.compute_revenue()))
  
