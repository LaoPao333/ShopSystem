from ErrorSearch.add_category_error import category_error
from Logic.Veriables import categoryes
def c_a_d(user_input, Shop):
    if user_input == "1":
        category = input("Введите название категории:")
        if category not in categoryes:
            category_error(category)
            Shop.add_category(category)
        else:
            print("Категория уже существует!")
    else:
        pass
