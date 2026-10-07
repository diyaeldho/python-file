# class Bank:
#     def __init__(self):                      #without encapsulation
#         self.balance=1000

# account=Bank()
# account.balance=-5000
# print(account.balance)


# class Bank:
#     def __init__(self):
#         self.__balance=1000                        #with capsulation
#     def set_balance(self,amount):
#         if amount>=0:
#             self.__balance=amount

#     def get_balance(self):
#         return self.__balance
    
# account= Bank()
# account.set_balance(-5000)
# print(account.get_balance())

# class Bank: 
#     def __init__(self):
#         self .__balance=1000                         #@property

#     @property
#     def balance(self):
#         return self .__balance
#     @balance.setter
#     def balance(self,amount):
#         if amount >=0:
#             self .__balance=amount
#         else:
#             print("Invalid balance. Balance cannot be negative")
# account=Bank()
# print("Initial Balance:",account.balance)

# account.balance=5000
# print("updated Balance:",account.balance)

# account.balance=-2000
# print("Final Balnce:",account.balance)

    