def factorial(n):
    '''
    Computes n factorial. For example:
    >>> factorial(6)
    720
    >>>
    '''
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

teste = factorial(5)
print(teste)

#

a = lambda x, y: x + y
r = a(2, 3)
print(r)




