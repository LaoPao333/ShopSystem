from Shop import shop
from Logic.Veriables import categoryes, products
def c_d_p(user_input, Shop):
    if user_input == "3":
        category = input(f"Выберите категорию из существующих {categoryes}")
        product = input(f"Выберите продукт из существующих {products}")
        Shop.delete_product(category, product)