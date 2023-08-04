try:
    i = 1 / 0
    print(i)
except Exception as e:
    print('出错了')
    print(e)

try:
    i = 1 / 1
    print(i)
except Exception as e:
    print('出错了')
    print(e)
else:
    print('正常运行')

try:
    i = 1 / 0
    print(i)
except Exception as e:
    print('出错了')
    print(e)
else:
    print('正常运行')
finally:
    print('最后执行')

try:
    i = 1 / 1
    print(i)
except Exception as e:
    print('出错了')
    print(e)
else:
    print('正常运行')
finally:
    print('最后执行')
