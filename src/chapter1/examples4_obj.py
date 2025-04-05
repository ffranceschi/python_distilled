class Stack:

    def __init__(self):
        self._items = [ ]

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>'

    def __len__(self):
        return len(self._items)

s = Stack()
s.push('Dave')
s.push(42)
s.push([3, 4, 5])
x = s.pop()
y = s.pop()

class MyStack(Stack):
    def swap(self):
        a = self.pop()
        b = self.pop()
        self.push(a)
        self.push(b)








