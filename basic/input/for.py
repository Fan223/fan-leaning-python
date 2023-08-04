for item in 'python':
    print(item)

for i in range(5):
    print(i)

# 不需要自定义变量可以写为 '_'
for _ in range(5):
    print("hello")

# for a in range(3):
a = 0
while a < 3:
    password = input('请输入密码: ')
    if password == '123':
        print('密码正确')
    else:
        print('密码错误')
    a += 1
else:
    print('你的密码已输入错误三次, 请 1 分钟再试')

for i in range(4):
    for j in range(4):
        print('*', end='\t')  # 不换行输出
    print()
