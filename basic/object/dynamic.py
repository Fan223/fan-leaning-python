class Student:
    def __init__(self, name, age):  # 初始化方法
        self.name = name
        self.age = age

    def eat(self):  # 实例方法
        print(self.name + '吃东西')


stu1 = Student('张三', 18)
stu1.gender = '女'
print(stu1.name, stu1.age, stu1.gender)


def show():
    print('show')


stu1.show = show
stu1.show()
