from typing import Any, List, Self


class Product:
    """Класс для представления информации о товаре"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, user_product: dict, products: List[Any] =None):
        name = user_product["name"]
        description = user_product["description"]
        price = user_product["price"]
        quantity = user_product["quantity"]

        if products:
            for product in products:
                if product.name == name:
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if self.__price > new_price:
                user_input = input("Вы действительно хотите понизить цену на товар? Введите y (yes) или n (no): ")
                if user_input == "y":
                    self.__price = new_price

            else:
                self.__price = new_price
