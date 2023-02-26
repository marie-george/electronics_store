import pytest
import os

from main_package.product_class import Item


def test_instantiate_from_csv_length():
    Item.instantiate_from_csv(os.path.join('test', 'test_items.csv'))
    assert len(Item.all_items) == 5


def test_instantiate_from_csv_examples():
    item1 = Item.all_items[0]
    assert item1.item_name == 'Смартфон'
    assert item1.item_price == 100
    assert type(item1.item_price) == int

@pytest.fixture
def coll():
    item = Item("Смартфон", 10000, 20)
    return item


def test_total_price_and_discount(coll):
    assert coll.calculate_total_price() == 200000
    assert coll.apply_discount() == 8500.0


def test_item_name_setter_less_10(coll):
    assert coll.item_name == "Смартфон"


def test_item_name_setter_more_10(coll):
    coll.item_name = 'СуперСмартфон'
    assert coll.item_name == 'Смартфон'


def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False

def test_repr(coll):
     assert repr(coll) == 'Item(Смартфон, 10000, 20)'

def test_str(coll):
    assert str(coll) == 'Смартфон'
