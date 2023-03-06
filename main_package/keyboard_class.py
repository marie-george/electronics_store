from main_package.product_class import Item
from main_package.mixin_lang_class import MixinLang


class KeyBoard(MixinLang, Item):
    pass


kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb)

print(kb.language)

kb.change_lang()
print(kb.language)

kb.language = 'CH'
