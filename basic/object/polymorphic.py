class Animal:
    def eat(self):
        print('动物')


class Dog(Animal):
    def eat(self):
        print('狗')


class Cat(Animal):
    def eat(self):
        print('猫')


class Person:
    def eat(self):
        print('人')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Person())