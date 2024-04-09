import math

class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name)>=3:
            self._name = name
        else:
            raise ValueError("Must be a string greater than two characters")

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        print("cannot change the name of the coffee")

    def customers(self):
        
        unique_customers = {order.customer for order in Order.all_orders if order.coffee == self}
        return list(unique_customers)
    
    def num_orders(self):
        num = [order.coffee for order in Order.all_orders if order.coffee == self]
        return len(num)
    
    def average_price(self):
        price = [order.price for order in Order.all_orders]

        if len(price) > 0:
            avg_price = sum(price)/len(price)
            truncated_average = math.floor(avg_price*10)/10.0
            formatted_average = f"{truncated_average:.1f}"
        
            return float(formatted_average)
        else:
            return 0.0

class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1<=len(name)<=15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters")
        
    def orders(self):
        return[order for order in Order.all_orders if order.customer == self]
        
    
    def coffees(self):
        unique_coffees = {order.coffee for order in Order.all_orders if order.customer == self}
        return list(unique_coffees)
    
    def create_order(self, coffee, price):
        new_order = Order(customer = self, coffee = coffee, price = price)
        return new_order
            
    
class Order:

    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        if isinstance(price, float) and 1.0<=price<=10.0:
            self._price = price
        else:
            raise ValueError("Price must be float between 1.0 and 10.0")
        
        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price (self, value):
        print("Price cannot be changed")   

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Customer not found")
        
    