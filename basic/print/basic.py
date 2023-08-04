# 输出数字
print(23)
print(11.323)

# 输出字符串
print('你好')
print("你好")

# 输出表达式
print(3 * 3)
print(5 % 2)

# 输出到文件中
fp = open('D://text.txt', 'a+')  # a+ 表示文件不存在则创建, 存在则在内容后面追加
print('test', file=fp)
print('++', file=fp)
fp.close()

# 不换行输出
print('hello', 'world')
