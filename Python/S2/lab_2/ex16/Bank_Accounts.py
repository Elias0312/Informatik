class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Error wrong amount!")

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
        else:
            print("Error wrong amount!")

    def get_balance(self):
        return f"{self.balance} EUR"
    
Yay = Account(100)

Yay.deposit(-3)
Yay.deposit(78.3)

print(Yay.get_balance())