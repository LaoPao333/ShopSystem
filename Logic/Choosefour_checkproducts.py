from ErrorSearch.check_products_error import product_check_error
from Logic.Veriables import categoryes, products
from Shop import shop
def c_c_p(user_input, Shop):
    if user_input == "4":
        category = input(f"Выберите категорию из существующих {categoryes}:")
        product_check_error(category)
        Shop.check_products(category)