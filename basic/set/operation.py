s1 = {10, 20, 30, 40}
print(10 in s1)
print(10 not in s1)

s1.add(50)
print(s1)
s1.update({80, 90}, [2, 3], ('num', 28), {'age': 18})
print(s1)

s1.remove('age')
print(s1)
# s1.remove(7)  # error
s1.discard(7)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
