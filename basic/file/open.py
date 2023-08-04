# file = open('a.txt', 'r', 1, 'UTF-8')
file = open('a.txt', encoding='UTF-8')
print(file.readlines())
file.close()
