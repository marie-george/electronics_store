from main_package.exceptions import InstantiateCSVError


def test_init_default_message():
    e = InstantiateCSVError()
    assert e.message == 'Файл item.csv поврежден'


def test_init_args():
    e = InstantiateCSVError('Отсутствует цена')
    assert e.message == 'Отсутствует цена'


def test_str():
    e = InstantiateCSVError()
    assert str(e) == 'Файл item.csv поврежден'