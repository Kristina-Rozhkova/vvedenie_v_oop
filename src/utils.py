import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict[Any, Any] | str:
    """Чтение данных из json-файла"""

    try:
        full_path = os.path.abspath(path)

        with open(full_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return "Файл не найден"


def create_objects_from_data(data: dict) -> list:
    """Создание экземпляров класса из данных"""
    categories = []
    for category in data:
        products = []

        for product in category["products"]:
            products.append(Product(**product))

        categories.append(Category(**category))

    return categories
