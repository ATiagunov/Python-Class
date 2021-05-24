class A:
    count = 0

    def __init__(self):
        A.count += 1

    def __del__(self):
        A.count -= 1

class B:
    _count = 0

    def __init__(self):
        B._count += 1

    def __del__(self):
        B._count -= 1
class C:
    __count = 0

    def __init__(self):
        C.__count += 1

    def __del__(self):
        C.__count -= 1



a = A()
b = A()
print(A.count)  # выведет 2
del a
print(A.count)  # выведет 1
A.count -= 1
# будет выведен 0, хотя остался объект b
print(A.count)
c = B()
d = B()
print(B._count)  # выведет 2
del c
print(B._count)  # выведет 1
B._count -= 1
# будет выведен 0, хотя остался объект b
print(B._count)
e = C()
f = C()
print(C.__count)  # выведет AttributeError
