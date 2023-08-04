class Student:
    address = '吉林'  # 类属性

    def __init__(self, name, age):  # 构造函数
        self.name = name
        self.age = age

    def eat(self):  # 实例方法
        print('吃东西')

    @staticmethod
    def method():  # 静态方法
        print('静态方法')

    @classmethod
    def cm(cls):  # 类方法
        print('类方法')


stu1 = Student('张三', 18)
print(id(stu1))
print(type(stu1))
print(stu1)

stu1.eat()
Student.eat(stu1)

stu1.method()
Student.method()

stu1.cm()
Student.cm()

print(stu1.name, stu1.age)
print(stu1.address)
print(Student.address)
