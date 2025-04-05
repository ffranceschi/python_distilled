items = [3, 4, 5]
d={}
d['x'], d['y'], d['z'] = items

#########
# expansion
items = [1, 2, 3]
a = [10, *items, 11]      # a = [10, 1, 2, 3, 11]       (list)
b = (*items, 10, *items)  # b = [1, 2, 3, 10, 1, 2, 3]  (tuple)
c = {10, 11, *items}
print(a)
print(b)
print(c)

###
#  Operadores com lista
a = [3, 4, 5]
b = [6, 7]
print(a + b)

#####
# Operadores com Set
a = {'a', 'b', 'c'}
b = {'c', 'd'}
print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference: {a - b}")
print(f"Difference Symmetric: {a ^ b}")




















