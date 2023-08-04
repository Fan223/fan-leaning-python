print('hello\nworld')  # 打印换行
# \t 打印空格 1 位, 因为一个制表位为 4 个字符, 而 \t 只会补满制表符, hell 占一个制表符, ooo 占一个制表符的 3 位, \t 补满剩下的 1 位
print('hellooo\tworld')
print('helloooo\tworld')  # \t 打印空格 4 位, helloooo 占满 2 个制表符, \t 新开一个制表符, 4 位
print('hello\rworld')  # world 对 hello 进行覆盖
print('hello\bworld')  # 退格 1 位, o 被退位

# 原字符, 不希望转义字符起作用, 在前面加上 r/R
print(r'hello\nworld')
