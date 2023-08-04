l1 = [10, 20, 30, 40, 50, 20]
l1.remove(20)
print(l1)
l1.pop()
print(l1)
l2 = l1[1:3:]
print(l1, l2)
l1.clear()
print(l1)
del l1
print(l1)  # error
