names = [ 'Dave', 'Paula', 'Thomas', 'Lewis' ]
print(names)

a = names[2]
names[2] = 'Tom'
print(names[-1])

print(names)

names = []
names = list()

address = ('www.python.org', 80)
host, port = address

print(f'site é {host} e a porta eh {port}')

names1 = { 'IBM', 'MSFT', 'AA' }
names2 = set(['IBM', 'MSFT', 'HPE', 'IBM', 'CAT'])

print(names1 & names2)

s = {
    'name' : 'GOOG',
    'shares' : 100,
    'price' : 490.10
    }

name = s['name']
print(name)

portfolio = [
    ('ACME', 50, 92.34),
    ('IBM', 75, 102.25),
    ('PHP', 40, 74.50),
    ('IBM', 50, 124.75)
]

total_shares = { s[0]: 0 for s in portfolio }
for name, shares, _ in portfolio:
    total_shares[name] += shares

print(f"total_shares = {total_shares}")

for n in range(1, 10):
    print(f'2 to the {n} power is {2**n}')


