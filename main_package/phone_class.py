from main_package.product_class import Item


class Phone(Item):
    all_items = []

    def __init__(self, item_name, item_price, item_quantity, number_of_sim):
        super().__init__(item_name, item_price, item_quantity)
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')


    def __repr__(self):
        return f'Phone({self.item_name}, {self.item_price}, {self.item_quantity}, {self.__number_of_sim})'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> str:
        if value > 0:
            self.__number_of_sim = value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

