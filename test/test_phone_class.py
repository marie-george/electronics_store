import pytest
from main_package.phone_class import Phone


@pytest.fixture
def coll2():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


def test_repr_phone(coll2):
    assert repr(coll2) == 'Phone(iPhone 14, 120000, 5, 2)'


def test_number_of_sim(coll2):
    coll2.number_of_sim = 1
    assert coll2.number_of_sim == 1

    with pytest.raises(ValueError):
        coll2.number_of_sim = 0

    with pytest.raises(ValueError):
        coll2.number_of_sim = -3

