class Customer:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__mobile_number = None

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_mobile_number(self):
        return self.__mobile_number


input_name = input('Enter your name: ')
input_email = input('Enter your email: ')
input_mobile_number = input('Enter your mobile number: ')
c = Customer()
c.set_name(input_name)
c.set_email(input_email)
c.set_mobile_number(input_mobile_number)
print('Name: ' + c.get_name())
print('Email: ' + c.get_email())
print('Mobile number: ' + c.get_mobile_number())
