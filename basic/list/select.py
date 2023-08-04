l1 = ['hello', 'world', 98, 'hello']
print(l1.index('hello'))
# print(l1.index('python'))  # error
print(l1.index('hello', 1))

# 负数为逆向获取
print(l1[-3])
# 正数即正向获取
print(l1[2])

# 切片
l2 = l1[0:2:1]
print(l1, id(l1), l2, id(l2))
# 任何一个参数都可省略
print(l1[0:2], l1[0:2:])
print(l1[:2:2])
print(l1[0::2])
print(l1[0:])
