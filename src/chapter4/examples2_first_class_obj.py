# __add__(self, other)
# __sub__(self, other)
# __mul__(self, other)
# __and__(self, other)
# __or__(self, other)

class Pessoa:
    def __init__(self, idade):
        self.idade = idade

    def __add__(self, pessoa):
        return Pessoa(self.idade + pessoa.idade)

    def __repr__(self):
        return f"idade: {self.idade}"

p1 : Pessoa = Pessoa(20)
repr(print(p1))
p2 : Pessoa = Pessoa(45)

p3 = p1 + p2
print(f"Idade da nova pessoa: {p3.idade}")

