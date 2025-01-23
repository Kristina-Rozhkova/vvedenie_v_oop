from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(first_product, second_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_product_new_product(data):
    result = Product.new_product(data)
    assert result.name == "Samsung Galaxy C23 Ultra"
    assert result.description == "256GB, Серый цвет, 200MP камера"
    assert result.price == 185000.0


def test_product_new_product_with_list(data, list_products):
    result = Product.new_product(data, list_products)
    assert result.name == "Samsung Galaxy C23 Ultra"
    assert result.quantity == 10
    assert result.price == 185000.0


def test_product_new_product_error(list_products):
    data = "Samsung Galaxy S23 Ultra; 256GB, Серый цвет, 200MP камера; 10; 185000.0"
    with pytest.raises(ValueError) as ex:
        Product.new_product(data, list_products)
    assert str(ex.value) == 'Новый продукт должен быть типа "dict", Вы добавили <class \'str\'>'


def test_product_price_setter_new_price(first_product):
    first_product.price = 185000
    assert first_product.price == 185000


def test_product_price_setter_min_price(first_product):
    with patch("builtins.input", return_value="y"):
        first_product.price = 800
        assert first_product.price == 800


def test_product_price_setter_negative_price(capsys, first_product):
    first_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
