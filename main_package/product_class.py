import csv
from exceptions import InstantiateCSVError

class Item:
    pay_rate = 0.85
    all_items = []

    def __init__(self, item_name, item_price, item_quantity):
        self.__item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.all_items.append(self)

    @property
    def item_name(self):
        return self.__item_name

    @item_name.setter
    def item_name(self, value) -> str:
        if len(value) > 10:
            print("Exception: наименование товара превышает 10 символов")
        else:
            self.__item_name = value

    @staticmethod
    def is_integer(value):
        value = float(value)
        if int(value) == value:
            return True
        return False

    @classmethod
    def instantiate_from_csv(cls, file):
        try:
            with open(file, 'r', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    price = row['price']
                    if price is None:
                        raise InstantiateCSVError
                    if cls.is_integer(price):
                        price = int(float(price))
                    quantity = row['quantity']
                    if quantity is None:
                        raise InstantiateCSVError
                    if cls.is_integer(quantity):
                        quantity = int(float(quantity))
                    else:
                        raise InstantiateCSVError
                    cls(row['name'], price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except InstantiateCSVError as e:
            print(e)
        # except InstantiateCSVError as e:
        #     print(e)

    def calculate_total_price(self):
        total_price = self.item_price * self.item_quantity
        return total_price

    def apply_discount(self):
        self.item_price = self.item_price * self.pay_rate
        return self.item_price

    def __repr__(self):
        return f'Item({self.__item_name}, {self.item_price}, {self.item_quantity})'

    def __str__(self):
        return self.__item_name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.item_quantity + other.item_quantity
        else:
            raise ValueError('Только объекты Item, Phone')














