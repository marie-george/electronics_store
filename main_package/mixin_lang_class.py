class MixinLang:
    def __init__(self, *args):
        self.__language = 'EN'
        super().__init__(*args)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'

