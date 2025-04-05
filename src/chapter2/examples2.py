# comprehension
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums if n > 2]
print(f"Squares: {squares}")


# [expression for item1 in iterable1 if condition1
#             for item2 in iterable2 if condition2
#             ...
#             for itemN in iterableN if conditionN ]


portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1 },
  {'name': 'MSFT', 'shares': 50, 'price': 45.67 },
  {'name': 'HPE', 'shares': 75, 'price': 34.51 },
  {'name': 'CAT', 'shares': 60, 'price': 67.89 },
  {'name': 'IBM', 'shares': 200, 'price': 95.25 }
]

# Collect all names ['IBM', 'MSFT', 'HPE', 'CAT', 'IBM' ]
names = [s['name'] for s in portfolio]
# Find all entries with more than 100 shares ['IBM']
more100 = [s['name'] for s in portfolio if s['shares'] > 100 ]
# Find the total shares*price
cost = sum([s['shares']*s['price'] for s in portfolio])
# Collect (name, shares) tuples
name_shares = [ (s['name'], s['shares']) for s in portfolio ]


#########

def toint(x):
    try:
        return int(x)
    except ValueError:
        return None

values = [ '1', '2', '-4', 'n/a', '-3', '5' ]
data1 = [ toint(x) for x in values ] # data1 = [1, 2, -4, None, -3, 5]
print(f"Data1: {data1}")
data2 = [ toint(x) for x in values if toint(x) is not None ] # data2 = [1, 2, -4, -3, 5]
print(f"Data2: {data2}")

#####

f = open('data.txt')
lines = (t.strip() for t in f)
comments = (t for t in lines if t[0] == '#')
for c in comments:
    print(c)







