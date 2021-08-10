import csv


class Product:

    def __init__(self, prod_name, prod_type, price):
        self.prod_name = prod_name
        self.prod_type = prod_type
        self.price = price

    def __str__(self):
        return f'{self.prod_type}: {self.prod_name} - price:{self.price}.'

    def __repr__(self):
        return self.__str__()


class Store:

    def __init__(self):
        self.list_product = []
        self.balance = 0
        self.import_times = 5

    def add_product(self, raw, times):
        self.list_product.extend([Product(raw['Наименование'],
                                          raw['Тип'],
                                          float(raw['Цена']))
                                 for i in range(times)])
        return self.list_product

    def read_csv(self):
        with open('inventory.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.DictReader(file, delimiter=',')
            for row in file_reader:
                self.add_product(row, self.import_times)

    def tipe_list(self, tipe=None):
        self.tipe_list = []
        for i in self.list_product:
            if tipe == i.prod_type:
                self.tipe_list.append(i)
            if tipe is None:
                self.tipe_list.append(i)
        return self.tipe_list

    def cost_products(self):
        self.cost_products = 0
        self.result = ''
        for prod in self.list_product:
            self.cost_products += prod.price
            self.result = f'Общая стоимость продуктов в наличии: {self.cost_products} грн.'
        return self.result

    def sale_product(self, name):
        self.prod_index = None
        for i, prod in enumerate(self.list_product):
            if prod.prod_name == name:
                self.prod_index = i
                break
        if self.prod_index is not None:
            self.balance += self.list_product[self.prod_index].price
            self.list_product.pop(self.prod_index)
            print(f'{name} - продан')
        else:
            print('Выберите доступный продукт')

    def balance(self):
        return self.balance


# Проверка работы
x = Store()
x.read_csv()
print(x.list_product)
print(x.cost_products())
x.sale_product('Эспрессо')
print(x.tipe_list('tea'))
print(x.balance)
