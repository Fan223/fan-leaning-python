d1 = {10, 20}
d2 = {10, 20}
print(d1 == d2)

d3 = {10, 20, 30, 40}
print(d1 != d3)

print(d1.issubset(d3))
print(d3.issuperset(d1))

d4 = {30, 40}
print(d1.isdisjoint(d3))
print(d1.isdisjoint(d4))
