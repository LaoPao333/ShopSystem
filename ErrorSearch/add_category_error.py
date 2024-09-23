from concurrent.futures import CancelledError
from Logic.Veriables import categoryes
def category_error(category): # Функция проверки на корректность ввода категории.
    if category.isalpha() and len(category) > 0:
        if category in categoryes: 
            raise CancelledError("Категория уже существует")
        else:
            pass
    else:
        raise CancelledError("Цифры или прочие символы (кроме букв) в создании категории \nИли же длина меньше нуля")