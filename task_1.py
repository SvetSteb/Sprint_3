import datetime as dt

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

# 1 Задание
    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items

# 2 Задание    
    def add_item_to_cheque(self, name):
        
        if  0 == len(name) or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

# 3 Задание
    def delete_item_from_check(self, name):

        if name in self.name_items:
            self.__name_items.remove(name)
            self.__number_items -= 1
        else:
            raise NameError('Позиция отсутствует в чеке')

# 4 Задание        
    def check_amount(self):
        total = []
        for item in self.name_items:
            total.append(self.__item_price.get(item))
        if self.number_items > 10:
            amount = sum(total) * 0.9
        else:
            amount = sum(total)
        return amount

# 5 Задание            
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price.get(item))
            else:
                continue
        if self.number_items > 10:
            tax_20 = (sum(total) * 0.9) * 0.2
        else:
            tax_20 = sum(total) * 0.2
        return tax_20

# 6 Задание
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.name_items:
            if self.__tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price.get(item))
            else:
                continue
        if self.number_items > 10:
            tax_10 = (sum(total) * 0.9) * 0.1
        else:
            tax_10 = sum(total) * 0.1
        return tax_10

# 7 Задание    
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

# 8 Задание
    @staticmethod
    def get_telephone_number(telephone_number):
        if type(telephone_number).__name__ != 'int':
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'

# 9 Задание (Дополнительно)   
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = dt.datetime.now()
        date = [['часы', (lambda x:x.hour)(now)], ['минуты', (lambda x: x.minute)(now)], ['день', (lambda x: x.day)(now)], ['месяц', (lambda x: x.month)(now)],  ['год', (lambda x: x.year)(now)]]
        for d in date:
            date_and_time.append(f'{d[0]}: {d[1]}')
        return date_and_time



#Tests
kassa = OnlineSalesRegisterCollector()
print(OnlineSalesRegisterCollector.get_date_and_time())
print(OnlineSalesRegisterCollector.get_telephone_number(456123123))
print(kassa.name_items)
print(kassa.number_items)
kassa.add_item_to_cheque('печенье')

kassa.add_item_to_cheque('чипсы')
kassa.add_item_to_cheque('кола')
kassa.add_item_to_cheque('печенье')
kassa.add_item_to_cheque('кефир')

print(kassa.name_items)
print(kassa.number_items)

""" kassa.add_item_to_cheque('печеньепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченьепеченье')
print(kassa.name_items)
print(kassa.number_items) """
kassa.delete_item_from_check('печенье')
print(kassa.name_items)
print(kassa.number_items)

print(kassa.check_amount()) #265
print(kassa.twenty_percent_tax_calculation()) #39

print(kassa.ten_percent_tax_calculation()) # 7

print(kassa.total_tax()) #46

print('--------------------------------------------------------')
new_cheque = OnlineSalesRegisterCollector()
new_cheque.add_item_to_cheque('чипсы')
new_cheque.add_item_to_cheque('кола')
new_cheque.add_item_to_cheque('печенье')
new_cheque.add_item_to_cheque('молоко')
new_cheque.add_item_to_cheque('кефир')
print(new_cheque.name_items)
print(new_cheque.number_items)
print(new_cheque.check_amount())
print(new_cheque.ten_percent_tax_calculation())
print(new_cheque.twenty_percent_tax_calculation())
print(new_cheque.total_tax())
print(new_cheque.get_telephone_number(1234567890))
print(new_cheque.get_date_and_time())
new_cheque.delete_item_from_check(('чипсы'))
print(new_cheque.name_items)
print(new_cheque.number_items)

