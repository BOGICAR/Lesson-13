import csv


class Store:

    def __init__(self):
        self.list_product = []
        self.import_times = 5

    def read_csv(self):
        with open('inventory.csv', 'r', encoding='utf-8') as f:
            file_reader = csv.reader(f, delimiter=',')
            next(file_reader)
            for i in file_reader:
                self.list_product.append(i)
            self.list_product *= self.import_times

    def tipe_list(self, tipe=None):
        self.tipe_list = []
        for line in self.list_product:
            if line[1] == tipe:
                self.tipe_list.append(line[0])
            if tipe == None:
                self.tipe_list.append(line[0])
        return self.tipe_list

    def cost_products(self):
        self.cost_products = 0
        self.result = ''
        for line in self.list_product:
            self.cost_products += int(line[2])
            self.result = f'Общая стоимость продуктов в наличии: {self.cost_products} грн.'
        return self.result

    def sale_product(self, name):
        self.sale_list = []
        for line in self.list_product:
            if line[0] == name:
                self.sale_list.append(line)
                self.list_product.remove(line)
                return self.sale_list

    def balance(self):
        self.balance = 0
        for list in self.sale_list:
            self.balance += int(list[2])
        return self.balance


class Product(Store):

    def properties(self, name):
        self.result = ''
        for line in self.list_product:
            if line[0] == name:
                self.result = line
                # self.result = f'Наименование: {line[0]}, ' \
                #               f'тип: {line[1]}, ' \
                #               f'цена: {line[2]}'
                return self.result

    def print_object(self, name):
        for line in self.list_product:
            if line[0] == name:
                self.result = f'Товар: {name}, цена: {line[2]}'
                return self.result


test = Product()
test.read_csv()
# Проверка работы
print(test.properties('Доппио'))
print(test.print_object('Earl Grey'))
print(test.tipe_list('coffee'))
print(test.cost_products())
print(test.sale_product('Имбирный чай'))
print(test.balance())
