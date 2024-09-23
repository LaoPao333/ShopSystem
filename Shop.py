from Logic.timer import timer
from Logic.Veriables import categoryes, products
class shop:
    def __init__(self):
        self.store = {}
    def add_category(self, category): # Функция добавления категории
            self.store[category] = {} 
            categoryes.append(category)
            print(f"Категория {category} добавлена")
            timer()

    def add_product(self, category, product, price): # Функция добавления продукта 
        products.append(product)
        self.store[category][product] = {"Цена >": price, "Категория >": category}
        print(self.store)
        timer()

    def delete_product(self, category, product): # Функция удаления продукта
        enter = input(f"Вы уверены что хотите удалить продукт {product} из категории {category} ? Нажмите Enter если да.")
        if enter == '':
            del self.store[category][product]
            print(f"Продукт {product} удалён.")
            timer()

    def check_products(self, category): # Функция проверки продуктов
        for i, char in enumerate(self.store[category]): # Использование цикла enumerate для вывода индекса и названия продукта
            if char == "":
                print("Продуктов нет!")
            timer()
            print(f"{i + 1}: {char}")
        timer()


