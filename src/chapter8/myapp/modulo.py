from dataclasses import dataclass

@dataclass()
class MyClass:
    x: int
    y: int

    @staticmethod
    def func():
        a = MyClass(1,2)
        print(vars(a))
