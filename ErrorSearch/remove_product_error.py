from concurrent.futures import CancelledError
from Logic.Veriables import categoryes, products
def product_error(category, product):
    if category in categoryes:
        if product in products:
            pass
        else:
            raise CancelledError("Проблемы которые могли возникнуть : \nПродукт не существует")
    else:
        raise CancelledError("Проблемы которые могли возникнуть : \nКатегория не существует")
    