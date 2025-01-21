def test_category_init(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 3


def test_category_count(category):
    assert category.category_count == 1


def test_product_count(category):
    assert category.product_count == 3
