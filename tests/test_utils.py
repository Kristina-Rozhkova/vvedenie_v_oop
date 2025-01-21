import os

from src.utils import read_json, create_objects_from_data


def test_read_json(return_data):
    """Тестирование корректного вывода данных из json-файла"""
    test_file_path = os.path.join(os.path.dirname(__file__), "test_products.json")

    result = read_json(test_file_path)

    assert result == return_data


def test_read_json_not_found_error():
    """Тестирование функции в случае неправильного указанного пути"""
    test_file_path = os.path.join(os.path.dirname(__file__), "incorrect_path.json")

    result = read_json(test_file_path)

    assert result == "Файл не найден"


def test_create_objects_from_data(return_data):
    """Тестирование корректного создания объектов класса"""
    result = create_objects_from_data(return_data)

    assert result[0].name == "Смартфоны"
    assert result[0].products[0] == {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
