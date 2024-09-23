from Shop import shop
from ErrorSearch.add_category_error import category_error
from ErrorSearch.add_product_error import product_error
from concurrent.futures import CancelledError
from Logic.Veriables import categoryes
from Logic.Chooseone_addcategory import c_a_d
from Logic.Choosetwo_addproduct import c_a_p
from Logic.Choosethree_deleteproduct import c_d_p
from Logic.Choosefour_checkproducts import c_c_p 
# Импорт функций / класса / переменных

o_c = True
Shop = shop()
while o_c == True:
    user_input = input("1 - Добавить категорию\n2 - Добавить продукт\n3 - Удалить продукт\n4 - Показать все продукты \n5 - Выйти \n>>>") 
    c_a_d(user_input, Shop) # Функция добавления категории.
    c_a_p(user_input, Shop) # Функция добавления продукта.
    c_d_p(user_input, Shop) # Функция удаления продукта.
    c_c_p(user_input, Shop) # Функция показа продуктов.

    if user_input == "5": # Выход из программы.
        print("Выход из программы...")
        o_c = False
    
# Меня просто даже радует что я эту часть кода написал организованно и структурированно 👍
# LaoPao | нет, в моем нике, изначально не должно было быть три тройки. 