items = ['fruit', 'book']
price = [100, 200]
l1 = zip(items, price)
print(l1, list(l1))

d1 = {item: price for item, price in zip(items, price)}
print(d1)
