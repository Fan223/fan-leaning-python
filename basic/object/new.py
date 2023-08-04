class Student:
    def __init__(self, name, age):
        print('init 创建的对象自身id', id(self))
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('new Student类', cls, id(cls))
        obj = super().__new__(cls)
        print('创建的对象id', id(obj))
        return obj


stu1 = Student('张安', 19)
print('Student类id', id(Student))
print('stu1对象id', id(stu1))
