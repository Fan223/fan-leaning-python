a = 3 + 4
print(a)

a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

a = 30
a += 10
print(a)
a *= 3
print(a, type(a))
a = a / 2
print(a, type(a))

a, b, c = 10, 20.3, 'ss'
print(a, type(a))
print(b, type(b))
print(c, type(c))
