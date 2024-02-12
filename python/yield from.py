def sub():
    yield 1
    yield 2


def link():
    res = yield from sub()
    print('res',res)

g = link()
for i in sub():
    print(i)