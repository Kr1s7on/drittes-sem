class Phone:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def get_phone_info(self):
        return 'The price of ' + self.__make + ' ' + self.__model + ' is $' + self.__price


input_make = input('Enter the make of the phone: ')
input_model = input('Enter the model of the phone: ')
input_price = input('Enter the price of the phone: ')
ph = Phone(input_make, input_model, input_price)
print(ph.get_phone_info())
