from examples1_basic import Account

class AccountPortfolio:
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def total_funds(self):
        return sum(account.inquiry() for account in self)
    def __len__(self):
        return len(self.accounts)
    def __getitem__(self, index):
        return self.accounts[index]
    def __iter__(self):
        return iter(self.accounts)

port = AccountPortfolio()
port.add_account(Account('Guido', 1000.0))
port.add_account(Account('Eva', 50.0))

print(port.total_funds()) # -> 1050.0
print(len(port))