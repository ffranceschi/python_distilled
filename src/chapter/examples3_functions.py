def remainder(a: int, b: int) -> int or None:
    q = a // b
    r = a - q * b
    return r

result = remainder(37, 15)
print(result)


def divide(a, b):
    q = a // b
    r = a - q * b
    return (q, r)

quotient, remainder = divide(1456, 33)

print(f"quotient = {quotient} remainder = {remainder}")





