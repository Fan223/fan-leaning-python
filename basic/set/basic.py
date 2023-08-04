s1 = {10, 20, 30, 40}
print(s1, type(s1))
s2 = {10, 10}
print(s2, type(s2))  # 重复元素只会存在一个

s3 = set(range(5))
print(s3, type(s3))

s4 = set((1, 2, 3))
print(s4, type(s4))

s5 = set('python')
print(s5, type(s5))
