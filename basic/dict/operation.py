d1 = {'张三': 100, '李四': 200}
d1['王五'] = 300
print(d1)

d1['王五'] = 333
print(d1)

del d1['王五']
print(d1)

d1.clear()
print(d1)

del d1
print(d1)  # error
