# # class NormalizedEmail(str):
# #     def __new__(cls, value):
# #         return super().__new__(cls, value.strip().upper())


# # email = NormalizedEmail("  shiv@EXAMPLE.COM  ")

# # print(email)  # shiv@example.com

# # class Product:
# #     # def __init__(self, name, price):
# #     #     self.name = name
# #     #     self.price = price

# #     def total_price(): # by default quantity is 1
# #     # def total_price(self, quantity = 1): # by default quantity is 1
# #         print("Total price is calculated")
# #         return ""

# # # laptop = Product("Laptop", 60000)
# # # mouse = Product("Mouse", 1000)

# # # print(laptop.name)           # Laptop
# # # print(mouse.name)            # Mouse
# # # print(laptop.total_price()) # 60000

# # # titalPrice = Product.total_price
# # # print(titalPrice())


# # class Product:
# #     currency = "INR"

# #     def __init__(self, name, price):
# #         self.name = name
# #         self.price = price

# #     # Receives the object
# #     def total_price(self, quantity):
# #         return self.price * quantity

# #     # Receives the class
# #     @classmethod
# #     def from_dict(cls, data):
# #         return cls(data["name"], data["price"])

# #     # Receives neither object nor class automatically
# #     @staticmethod
# #     def is_valid_price(value):
# #         return isinstance(value, (int, float)) and value >= 0

# # product = Product.from_dict({
# #     "name": "Keyboard",
# #     "price": 2500
# # })

# # print(product.total_price(2))       # 5000
# # print(Product.is_valid_price(10))  # False


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")

#         self._price = value

# product = Product("Mouse", 1000)

# product.price = 1500
# print(product.price)  # 1500

# product.price = -100  # ValueError


class EmailNotifier:
    def send(self):
        print("Sending email")


class SMSNotifier:
    def send(self):
        print("Sending SMS")


class Notifier(EmailNotifier, SMSNotifier):
    pass


Notifier().send()  # Sending email
print(Notifier.__mro__)