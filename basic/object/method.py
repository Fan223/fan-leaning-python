class Student:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.name + other.name


stu1 = Student('张三')
stu2 = Student('李四')
print(len(stu1))
print(len(stu2))

print(stu1.__add__(stu2))
