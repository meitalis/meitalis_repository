
class BankAccount():
    #total_credit = 2000
    bank_name = "PyPay"

    def __init__(self, balance = 0):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def print_balance(self,):
        print(" balance:", self._balance)
    #
    # @classmethod
    # def get_credit(cls):
    #     return cls.total_credit

    # def withdraw(self, amount):
    #     if amount > 0:
    #         if amount > self.balance + self.get_credit():#self.total_credit:
    #             print("Insufficient funds")
    #         else:
    #             self.balance -= amount
    #     else:
    #         print("Invalid withdrawal amount:", amount)
    #
    #     print("[withdraw] balance:", self.balance)


b1 = BankAccount()
b1._balance = 200
b1.print_balance()

b2 = BankAccount(1000)
b2.withdraw(200)
b2.print_balance()

BankAccount.bank_name = "1111"
print(BankAccount.bank_name)
print(b2.bank_name)
#not good - its another bank_name attribute but just for b2 , it is not belong to the class
b2.bank_name = "2222"
print(BankAccount.bank_name)
print(b2.bank_name)
print(b1.bank_name)