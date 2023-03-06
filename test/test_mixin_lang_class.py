import pytest
from main_package.mixin_lang_class import MixinLang

@pytest.fixture
def coll():
    lang = MixinLang()
    return lang


def test_init(coll):
    assert coll.language == 'EN'

    with pytest.raises(AttributeError):
        coll.language = 'CH'


def test_change_lang(coll):
    coll.change_lang()
    assert coll.language == 'RU'
    coll.change_lang()
    assert coll.language == 'EN'




