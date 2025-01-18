from datetime import date, timedelta
import random

class Client:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    name = ""
    id_number = 0
    number_of_rents = 0
    rented_products = [ ]

    def get_number_of_rents(self):
        return self.number_of_rents


    def get_rented_products(self):
        return self.rented_products


    # This function simulates the rental of a product by a client.
    def rent_product(self, system, name_of_product):
        if not system.is_client_in_clients(self):
            system.add_client(self)

        products = system.get_products()
        if name_of_product in products:
            # The value in products is either a date or an empty string.
            # If the item is rented, the value is a date.
            if products[name_of_product][0]:
                print("Now this product is not available," 
                      " it will be available again on "
                      + products[name_of_product][0].strftime("%d/%m/%y"))
            else:
                # Simulation of how many days a client wants to rent a product.
                # The maximum rental period is 365 days.
                days_of_rent = random.randint(1,365)
                return_date = date.today() + timedelta(days_of_rent)

                products[name_of_product][0] = return_date
                self.rented_products.append(name_of_product)
                self.number_of_rents += 1
                print("You have rent a " + name_of_product
                      + " for a " + str(days_of_rent) + " days"
                      + " and you need to bring it back on "
                      + return_date.strftime("%d/%m/%y"))
        else:
            system.add_desired_product(name_of_product)
            print("There is no such product to rent, but "
                  + f'{name_of_product}'
                  + " is added now to the wishlist.")


    # This function simulates the process of the client returning a product.
    def return_product(self, system):
        product_to_return = random.randint(0, len(self.rented_products) - 1)
        print("I want to return " + f'{self.rented_products[product_to_return]}')
        # The value in products is either a date or an empty string.
        # If the item is returned, the value must be an empty string.
        system.products[self.rented_products[product_to_return][0]] = " "
        returned_product = self.rented_products.pop(product_to_return)
        print("The " + f'{returned_product}' + " was successfully returned.")


    def is_regular_customer(self, system):
        print("Am I a regular customer?")
        if system.is_client_in_clients(self):
            if self.number_of_rents >= 5:
                print("You are a regular customer!")
            else:
                print("You are not a regular customer yet,"
                      f" you need to rent {5 - self.number_of_rents} times"
                      " more to become a regular customer.")
        else:
            print('You are not a client of "LeihenWaren" yet.')


    def get_product_price(self, system, name_of_product):
        if system.get_product_price(name_of_product):
            if self.number_of_rents >= 5:
                # For a regular client there is 15% discount
                price_of_product = system.get_product_price(name_of_product) - 0.15 * system.get_product_price(name_of_product)
                print(f"The rental price of {name_of_product} is {price_of_product} per day")
            else:
                price_of_product = system.get_product_price(name_of_product)
                print(f"The rental price of {name_of_product} is {price_of_product} per day")
        else:
            print("There is no such product to rent")