a, b = 10, 20
print(a > b)
print(a <= b)

# 一个变量由 标识、类型、值 三部分组成, == 比较的是值, is 比较的是标识, is not 即标识不相等
print(a == b)
print(a != b)

c = 10
print(a == c, id(a))
print(a is c, id(c))
print(a is not c)

list1 = [11, 22, 33]
list2 = [11, 22, 33]
print(list1 == list2, id(list1))
print(list1 is list2, id(list2))
print(list1 is not list2)
