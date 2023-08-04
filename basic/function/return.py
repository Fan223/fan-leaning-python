def f1(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


result1 = f1([1, 3, 2, 3, 4, 5])
print(result1, type(result1))


def f2(num):
    return num


result2 = f2(123)
print(result2, type(result2))
result3 = f2('123')
print(result3, type(result3))
