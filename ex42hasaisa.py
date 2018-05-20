#!/usr/bin/env python
# coding=utf-8

class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

lyndon = Employee('lyndon', 6000)
fox = Dog('fox')
petty = Cat('petty')
no1 = Salmon()
no2 = Halibut()
lyndon.pet = fox

print """
There is a person, named %s.
He has a pet: %s.
He also feed two Fishes: %s, %s.
Around his yard, There is Cat: %s.
""" % (lyndon, lyndon, no1, no2, petty)

