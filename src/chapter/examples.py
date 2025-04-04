x: int = 42
print(x)
a: int = 1
b: int = 2

maxval = a if a > b else b
print(maxval)
#
with open('data.txt') as file:
    for line in file:
        print(line, end='')
#
print('\n\n\n')
with open('data.txt') as file:
    while (chunk := file.read(1)):
        print(chunk, end='')

#

year: int = 2000
numyears = 2010
rate = 1
principal = 1

with open('out.txt', 'wt') as out:
    while year <= numyears:
        principal = principal * (1 + rate)
        print(f'{year:>3d} {principal:0.2f}', file=out)
        year += 1