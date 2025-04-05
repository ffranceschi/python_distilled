class Manager:
    def __init__(self, x):
        self.x = x
    def yow(self):
        pass
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, ty, val, tb):
        print("exit")
        pass

with Manager(42) as m:
    print("dentro do context manager")
    m.yow()

class DeviceError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg

try:
    file = open('foo.txt', 'rt')
except FileNotFoundError as e:
    print("Well, that didn't work.")
    # raise DeviceError(1, 'Nao encontrado')


