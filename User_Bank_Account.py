class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)


    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_balance(self):
        return self.account.balance


