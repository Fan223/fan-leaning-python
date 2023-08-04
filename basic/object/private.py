class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.age)


stu1 = Student('张三', 20)
print(stu1.name)
# print(stu1.__age)  # error
print(dir(stu1))
print(stu1._Student__age)
