class System:

    def __init__(self, products):
        self.products = products

    clients = [ ]
    products = { }
    desired_products = [ ]

    def get_products(self):
        return self.products


    def get_clients(self):
        return self.clients


    def is_client_in_clients(self, client):
        counter = 0
        for each_client in self.clients:
            if each_client.id_number == client.id_number:
                counter += 1
        if counter:
            return True
        else:
            return False


    def add_client(self, new_client):
        if not self.is_client_in_clients(new_client):
            self.clients.append(new_client)
            print("The client successfully added in database ")
        else:
            print("This client is already in database")


    def remove_client(self, client):
            if self.is_client_in_clients(client):
                self.clients.remove(client)
            else:
                print(f"There is no client with name {client.name} and id {client.id_number} in database")


    def add_product(self, name_of_product):
        #if there is no data, then product is available
        self.products[name_of_product] = ""


    def add_desired_product(self, name_of_product):
        self.desired_products.append(name_of_product)


    def get_product_price(self, name_of_product):
        if name_of_product in self.products:
            return self.products[name_of_product][1]
        else:
            return 0