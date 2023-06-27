class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate


# Example usage
account = Account("Ashish", 5000)
print("Account Title:", account.title)
print("Account Balance:", account.balance)

savings_account = SavingsAccount("Ashish", 5000, 5)
print("Savings Account Title:", savings_account.title)
print("Savings Account Balance:", savings_account.balance)
print("Savings Account Interest Rate:", savings_account.interestRate)