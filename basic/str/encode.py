s1 = '你好'
b1 = s1.encode('GBK')
print(b1)  # 一个中文占两个字节
b2 = s1.encode('UTF-8')
print(b2)  # 一个中文占三个字节

# 解码格式要和编码格式相同
print(b1.decode(encoding='GBK'))
print(b2.decode(encoding='UTF-8'))
