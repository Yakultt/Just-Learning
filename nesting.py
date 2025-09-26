class A:
    A = 'A'

    def __init__(self):
        self.A += 'A'


class B(A): pass

a = A()
b = B()

print(b.A)