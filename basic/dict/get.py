d1 = {'张三': 100, '李四': 200}
print(d1['张三'])
print(d1.get('张三'))

# print(d1[2])  # error
print(d1.get(2))
print(d1.get(2, 99))
