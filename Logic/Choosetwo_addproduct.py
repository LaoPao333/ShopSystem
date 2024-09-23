from Logic.Veriables import categoryes
from ErrorSearch.add_product_error import product_error
def c_a_p(user_input, Shop): # Функция добавления продукта
    if user_input == "2":
        category = input(f"Введите категорию из существующих {categoryes}: ")
        product = input("Введите название продукта :")
        price = input("Введите цену :")
        product_error(category, product, price) # Функция проверки на ошибки
        Shop.add_product(category, product, price)
    else:
        pass
        