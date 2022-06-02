class ShoppingCenter:

    def __init__(self, number=0, name="none", country: str = "from space"):
        self.__number = number
        self.__name = name
        self.__country = country

    def get_shopping_center(self):
        return self.__number, self.__name, self.__country


class Product(ShoppingCenter):
    def __init__(self, number, name, country, price):
        super().__init__(number, name, country)
        self.__price = price

    def get_product(self):
        return self.__name, self.__number, self.__country, self.__price


class Customer(ShoppingCenter):
    def __init__(self, number, name, country, regular_customer: bool, contacts):
        super().__init__(number, name, country)
        self.__regular_customer = regular_customer
        self.__contacts = contacts

    def get_customer(self):
        return  self.__name, self.__number,  self.__country, self.__regular_customer, self.__contacts


class Shop(ShoppingCenter):
    def __init__(self, number, name, country, specialization):
        super().__init__(number, name, country)
        self.__specialization = specialization

    def get_shopping_center(self):
        return self.__name, self.__number, self.__country, self.__specialization


