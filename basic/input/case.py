money = 1000
s = int(input('请输入取款金额: '))
if money >= s:
    money -= s
    print('余额为', money)
else:
    print('余额不足')

score = int(input('请输入成绩: '))
if 90 <= score <= 100:
    print('优秀')
elif 80 <= score < 90:
    print('良好')
elif 70 <= score < 80:
    print('一般')
elif 60 <= score < 70:
    print('及格')
elif score < 60:
    print('不及格')
else:
    print('成绩不在范围内')

money = float(input('请输入购物金额: '))
vip = input('你有会员吗?y/n')
if vip == 'y':
    if money >= 200:
        print('八折')
    elif money < 200:
        print('九折')
    else:
        print('不打折')
else:
    if money >= 200:
        print('九五折')
    else:
        print('不打折')

a = int(input('输入第一个整数: '))
b = int(input('输入第二个整数: '))
print(str(a) + '大于等于' + str(b) if a >= b else str(a) + '小于' + str(b))

vip = input('你有会员吗?y/n')
if vip == 'y':
    pass
else:
    pass
