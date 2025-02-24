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
    assert str(ex.value) == "Новый продукт должен быть типа \"dict\", Вы добавили <class 'str'>"


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
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_product_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(first_product, second_product):
    result = first_product + second_product
    assert result == 2580000.0


def test_product_add_error(first_product, lawn_grass2):
    with pytest.raises(TypeError) as ex:
        first_product + lawn_grass2
    assert str(ex.value) == "К продукту класса Product можно добавить только продукт класса Product"


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Iphone 15"
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "15"
    assert smartphone1.memory == 512
    assert smartphone1.color == "Gray space"


def test_smartphone_add(smartphone1, smartphone2):
    result = smartphone1 + smartphone2
    assert result == 2114000.0


def test_smartphone_add_error(smartphone1, first_product):
    with pytest.raises(TypeError) as ex:
        smartphone1 + first_product
    assert str(ex.value) == "К продукту класса Smartphone можно добавить только продукт класса Smartphone"


def test_lawn_grass_init(lawn_grass1):
    assert lawn_grass1.name == "Газонная трава"
    assert lawn_grass1.country == "Россия"
    assert lawn_grass1.germination_period == "7 дней"
    assert lawn_grass1.color == "Зеленый"


def test_lawn_grass_add(lawn_grass1, lawn_grass2):
    result = lawn_grass1 + lawn_grass2
    assert result == 16750.0


def test_lawn_grass_add_error(lawn_grass1, smartphone1):
    with pytest.raises(TypeError) as ex:
        lawn_grass1 + smartphone1
    assert str(ex.value) == "К продукту класса LawnGrass можно добавить только продукт класса LawnGrass"


def test_print_mixin_product(capsys):
    Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)'


def test_print_mixin_smartphone_and_lawn_grass(capsys, smartphone1, lawn_grass1):
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[0] == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"
    assert message.out.strip().split("\n")[1] == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


def test_product_init_error(capsys):
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
