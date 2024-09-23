from concurrent.futures import CancelledError
from Logic.Veriables import categoryes, products

def product_error(category, product, price):
    try:
        int(price)
    except:
        raise CancelledError("Проблемы которые могли возникнуть : \nЦена должна быть целым числом")
    if len(product) > 0:
        if product not in products:
            if category in categoryes:
                if int(price) > 0:
                    pass
                else:
                    raise CancelledError("Проблемы которые могли возникнуть : \nЦена должна быть больше нуля")
            else:
                raise CancelledError("Проблемы которые могли возникнуть : \nКатегория должна существовать\nЦена должна быть больше нуля")
        else:
            raise CancelledError("Проблемы которые могли возникнуть : \nПродукт уже существует\nЦена должна быть больше нуля")
    else:
        raise CancelledError("Проблемы которые могли возникнуть : \nВ продукте можно использовать только буквы\n"
                             "Длина должна быть больше нуля\nЦена должна быть больше нуля")