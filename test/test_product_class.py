from product_class import Item


def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000
    assert item.apply_discount() == 8500.0

