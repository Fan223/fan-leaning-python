name = '张三'
age = 18
print('我叫%s, 今年%d岁' % (name, age))

print('%10i' % 99)
print('%.3f' % 3.1415926)

print('我叫{0}, 今年{1}岁, {0}'.format(name, age))
print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))  # 3 位数
print('{0:.3f}'.format(3.1415926))  # 3 位小数
print('{:.3f}'.format(3.1415926))
print('{:10.3f}'.format(3.1415926))

print(f'我叫{name}, 今年{age}岁')
