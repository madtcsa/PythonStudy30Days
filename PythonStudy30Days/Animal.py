#!/usr/bin/env python3


class Animal(object):
    def run(self):
        print('Animal is running....')


class Dog(Animal):
    pass


class Cat(Animal):
    def run(self):
        print('Cat is running.....')


a = Animal()
d = Dog()
c = Cat()


def run_twice(animal):
    animal.run()
    animal.run()


# print('a is Animal?', isinstance(a, Animal))
# print('a is Dog?', isinstance(a, Dog))
# print('a is Cat?', isinstance(a, Cat))

# print('d is Animal?', isinstance(d, Animal))
# print('d is Dog?', isinstance(d, Dog))
# print('d is Cat?', isinstance(d, Cat))

run_twice(c)


class Student(object):
    pass


s = Student()
s.name = 'Michael'
print(s.name)


def set_age(self, age):
    sel.age = age


from types import MethodType
s, set_age = MethodType(set_age, s)
s.set_age(25)
