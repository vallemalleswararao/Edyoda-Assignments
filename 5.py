class Account:
    def __init__(self, balance):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def interestAmount(self):
        return self.balance * self.interest_rate


# Example usage
account = Account(1000)
print("Initial Balance:", account.getBalance())

account.deposit(500)
print("After Deposit:", account.getBalance())

account.withdrawal(200)
print("After Withdrawal:", account.getBalance())

savings_account = SavingsAccount(2000, 0.05)
print("Savings Account Balance:", savings_account.getBalance())
print("Interest Amount:", savings_account.interestAmount())