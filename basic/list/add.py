l1 = []
l1.append(1)
print(id(l1))
l1.append(2)
print(l1, id(l1))

l2 = [3, 4]
l1.append(l2)
l1.extend(l2)
print(l1)

l1.insert(1, 10)
print(l1)

l3 = [True, False]
l1[1:] = l3
print(l1)
