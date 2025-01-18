from system import System
from client import Client

mark = Client("Mark", 1)

system = System({"saw": ["", 12.3],
                 "jigsaw": ["", 6.5],
                 "screwdriver": ["", 7.8]})

system_1 = System({"saw": ["", 12.3],
                 "jigsaw": ["", 6.5],
                 "screwdriver": ["", 7.8],
                 "chainsaw": ["", 3.6],
                 "ladder": ["", 3.6]})

christoph = Client("Christoph", 2)
christoph.rent_product(system_1, "saw")
christoph.rent_product(system_1, "jigsaw")
christoph.rent_product(system_1, "screwdriver")
christoph.rent_product(system_1, "chainsaw")
christoph.rent_product(system_1, "ladder")
christoph.get_product_price(system_1, "screwdriver")


mark.rent_product(system, "saw")

mark.rent_product(system, "saw")

mark.rent_product(system, "drill")

print(mark.get_rented_products())

mark.return_product(system)

print(mark.get_rented_products())

mark.is_regular_customer(system)

mark.get_product_price(system, "screwdriver")
christoph.get_product_price(system_1, "screw")

lena = Client("Lena", 3)

system_1.remove_client(lena)

