from contextlib import contextmanager

@contextmanager
def manager():
    print("Entering")
    try:
        yield 'somevalue'
    except Exception as e:
        print("An error occurred", e)
    finally:
        print("Leaving")

with manager() as val:
    print(val)

with manager() as val:
    print(int(val))