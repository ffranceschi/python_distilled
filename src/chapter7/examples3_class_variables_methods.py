class Account2:
    num_accounts = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        Account2.num_accounts += 1
    def __repr__(self):
        return f'{type(self).__name__}({self.owner!r}, {self.balance!r})'
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.deposit(-amount) # Must use self.deposit()
    def inquiry(self):
        return self.balance


a = Account2('Guido', 1000.0)
b = Account2('Eva', 10.0)
print(Account2.num_accounts)


# ------

class Account2:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext('owner'), float(doc.findtext('amount')))

data = '''
<account>
<owner>Guido</owner>
<amount>1000.0</amount>
</account>
'''
a2 = Account2.from_xml(data)

print(vars(a2))

# ------

class Ops:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def sub(x, y):
        return x - y

a3 = Ops.add(2, 3)
b3 = Ops.sub(4, 5)


