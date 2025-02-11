import pytest

from src.product import Product


def test_category_init(category):
    """Тестирование инициализации экземпляров класса Category"""
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products_in_list) == 3

    assert category.category_count == 1
    assert category.product_count == 3


def test_add_product(category):
    """Тестирование добавления продукта в список продуктов"""
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category.add_product(product)
    # результат должен быть равен 7, потому что при запуске данного теста, в классе Category
    # переменная category инициализируется как новый экземпляр класса
    assert category.product_count == 7


def test_add_product_error(category):
    """Тестирование выпадения ошибки при добавлении продукта в список продуктов"""
    with pytest.raises(TypeError) as ex:
        category.add_product(1)
    assert str(ex.value) == "Нужно добавить продукт из класса Product или из его дочерних классов"


def test_category_products(category):
    """Тестирование вывода информации о продуктах"""
    information = category.products
    return_str = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )

    assert information == return_str


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


def test_product_iterator(product_iterator):
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)

    iterator = product_iterator.__iter__()
    assert product_iterator.index == 0


def test_category_add_smartphone(category, smartphone1):
    category.add_product(smartphone1)
    assert category.product_count == 23


def test_category_add_lawn_grass(category, lawn_grass2):
    category.add_product(lawn_grass2)
    assert category.product_count == 27
