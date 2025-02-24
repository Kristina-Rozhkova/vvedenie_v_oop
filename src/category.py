from abc import ABC, abstractmethod

from src.product import Product


class BaseClass(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Category(BaseClass):
    """Класс с информацией о товарах в соответствующей категории"""

    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0
    quantity_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        for product in self.__products:
            self.quantity_count += product.quantity
        return f"{self.name}, количество продуктов: {self.quantity_count} шт."

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Нужно добавить продукт из класса Product или из его дочерних классов")

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_in_list(self):
        return self.__products


class ProductIterator:

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


class Order(BaseClass):
    product: Product
    quantity: int
    cost: float

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.cost = self.calculate_cost()

    def __str__(self):
        return (f"Товар: {self.product.name}, \n"
                f"Описание: {self.product.description}, \n"
                f"Количество: {self.quantity} шт., \n"
                f"Цена за 1 единицу: {self.product.price} руб., \n"
                f"Общая стоимость: {self.cost}")

    def calculate_cost(self):
        return self.quantity * self.product.price
