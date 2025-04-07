nums = [1, 2, 3, 4, 5]

squares = (x*x for x in nums)
for n in squares:
    print(n)
# ------

squares = map(lambda x: x*x, nums)
for n in squares:
    print(n)

# --
for n in filter(lambda x: x > 2, nums):
    print(n)

# ---
from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print(f"Resultado: {total}")