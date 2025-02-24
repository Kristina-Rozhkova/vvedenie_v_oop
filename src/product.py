from abc import ABC, abstractmethod
from typing import Any, List


class BaseProduct(ABC):
    """Базовый абстрактный класс для класса продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, PrintMixin):
    """Класс для представления информации о товаре"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError("К продукту класса Product можно добавить только продукт класса Product")

    @classmethod
    def new_product(cls, user_product: dict, products: List[Any] = None):
        if isinstance(user_product, dict):
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

        type_new_product = type(user_product)
        raise ValueError(f'Новый продукт должен быть типа "dict", Вы добавили {type_new_product}')

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


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("К продукту класса Smartphone можно добавить только продукт класса Smartphone")


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("К продукту класса LawnGrass можно добавить только продукт класса LawnGrass")
