#!/usr/bin/env python
# coding=utf-8

# Animal is-a object
class Animal(object):
    pass
# dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def bark():
        print 'WANG~' * 3

    def wave_tail():
        print 'wave its tail happily'
# cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound():
        print 'MIAO~~' * 3

    def rub():
        print 'The cat is rubbing on your pants'
#Person is-a object
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

    def walk():
        print 'walk around'

    def sing():
        print 'I love you, look at me.'

    def eat(self):
        print 'eating'
        return 'eating'

    def smell(self):
        print 'smelling'
        return 'smelling'

    def see(self):
        print "look around"
        return "look around"

    def hear(self):
        print 'hearing carefully'
        return 'hearing carefully'

    def touch():
        print 'touching and feeling'
#Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

    def work(self):
        print 'working'
        return 'working'

    def ask():
        print 'asking'

    def code():
        print 'coding'

class Fish(object):
    def __init__(self):
        print 'initilize a fish'

    def swim():
        print 'swimming'

    def hunt():
        print 'hunting'

    def eat():
        print 'eating'
#Salmon is-a Fish
class Salmon(Fish):
    def __init__(self):
        print 'initilize a Salmon...'

    def scale(self):
        print 'small scales'
        return 'small scales'
#Halibut is-a Fish
class Halibut(Fish):
    def __init__(self):
        print 'initilize a Halibut'

    def scale(self):
        print 'big scales'
        return 'big scales'

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
""" % (lyndon.name, lyndon.pet.name, no1, no2, petty.name)

print """
lyndon can: %s, %s, %s. %s
no1 has: %s
no2 has: %s
""" % (lyndon.hear(), lyndon.eat(), lyndon.see(), lyndon.smell(), no1.scale(), no2.scale())
