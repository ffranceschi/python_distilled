from typing import *

def remainder(a: int, b: int) -> int or None:
    q = a // b
    r = a - q * b
    return r

result = remainder(37, 15)
print(result)


def divide(a: int, b: int=3) -> Tuple[int, int] or None:
    q = a // b
    r = a - q * b
    return (q, r)

quotient, remainder = divide(1456, 33)

quotient, remainder = divide(a=10,b=8)

print(f"quotient = {quotient} remainder = {remainder}")





