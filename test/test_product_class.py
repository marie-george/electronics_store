import pytest
import os

from main_package.product_class import Item
from main_package.phone_class import Phone
from main_package.exceptions import InstantiateCSVError


def test_instantiate_from_csv_correct_file():
    Item.instantiate_from_csv('test_items.csv')
    assert len(Item.all_items) == 5
    item1 = Item.all_items[0]
    assert type(item1.item_name) == str
    assert type(item1.item_quantity) == int
    assert type(item1.item_price) == int


def test_instantiate_from_csv_corrupted_file():
    assert Item.instantiate_from_csv('test_items_2.csv') == print('Файл item.csv поврежден')


def test_instantiate_from_csv_file_not_found():
    assert Item.instantiate_from_csv('test_items_3.csv') == print('Отсутствует файл csv')



@pytest.fixture
def coll():
    item = Item("Смартфон", 10000, 20)
    return item


def test_total_price_and_discount(coll):
    assert coll.calculate_total_price() == 200000
    assert coll.apply_discount() == 8500.0


def test_item_name_setter_less_10(coll):
    coll.item_name = "Mobile"
    assert coll.item_name == "Mobile"


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


def test_add():
    item1 = Item("Смартфон", 10000, 5)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 10
    assert phone1 + item1 == 10

    with pytest.raises(ValueError):
        phone1 + 100



