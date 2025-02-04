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


def test_category_products(category):
    """Тестирование вывода информации о продуктах"""
    information = category.products
    return_str = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )

    assert information == return_str
