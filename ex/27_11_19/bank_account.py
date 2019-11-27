class BankAccount():
    total_credit = 2000

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("[deposit] balance:", self.balance)

    @classmethod
    def get_credit(cls):
        return cls.total_credit

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.balance + self.get_credit():#self.total_credit:
                print("Insufficient funds")
            else:
                self.balance -= amount
        else:
            print("Invalid withdrawal amount:", amount)

        print("[withdraw] balance:", self.balance)


b1 = BankAccount("b1")
b1.deposit(1000)
b1.withdraw(4000)
b2 = BankAccount("b2")
b3 = BankAccount("b3")