import os

names = os.listdir('.')
for name in names:
    print(name)

home = os.getenv('HOME')
print(home)