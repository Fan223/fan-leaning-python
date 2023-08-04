t1 = ('python', 99)
print(t1, type(t1))
t2 = ('python',)
print(t2, type(t2))

t3 = 'python',
print(t3, type(t3))

t4 = tuple(('python', 'world', 98))
print(t4, type(t4))

for item in t4:
    print(item)
