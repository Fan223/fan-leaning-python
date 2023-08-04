# coding:utf-8
name = '张三'
age = 18
print(type(name), type(age))
# print('我叫' + name + '今年' + age + '岁')  # error
print('我叫' + name + '今年' + str(age) + '岁')

# str() 函数, 将其他类型转成 str
s1 = 128
s2 = 98.7
s3 = True
print(type(str(s1)), type(str(s2)), type(str(s3)))

# int() 函数, 将其他类型转成 int
s4 = '23'
s5 = '23.2'
print(int(s2), type(int(s2)))  # float 转成 int 类型, 只保留整数部分
print(int(s3), type(int(s3)))  # bool 转成 int 类型, True 为 1, False 为 0
print(int(s4), type(int(s4)))  # str 转成 int 类型, 字符串要为整数数字串
# print(int(s5), type(int(s5)))  # error

# float() 函数, 将其他类型转成 float
print(float(s1), type(float(s1)))
print(float(s3), type(float(s3)))
print(float(s4), type(float(s4)))
print(float(s5), type(float(s5)))
