class Phone:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        if price.isnumeric():
            self.__price = price
        else:
            self.__price = 0
            exit('Price should be in numbers.')

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def get_phone_info(self):
        return 'The price of ' + self.__make + ' ' + self.__model + ' is $' + str(self.__price)


input_make = input('Enter the make of the phone: ')
input_model = input('Enter the model of the phone: ')
input_price = input('Enter the price of the phone: ')
ph = Phone()
ph.set_make(input_make)
ph.set_model(input_model)
ph.set_price(input_price)
print(ph.get_phone_info())
