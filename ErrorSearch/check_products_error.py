from concurrent.futures import CancelledError
from Logic.Veriables import categoryes
def product_check_error(category):
    if category in categoryes:
        if category.isalpha() and len(category) > 0:
            pass
        else:
            raise CancelledError("Цифры или прочие символы кроме букв. Или же длина категории меньше нуля")
    else:
        raise CancelledError("Категория не существует")
    