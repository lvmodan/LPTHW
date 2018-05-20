#!/usr/bin/env python
# coding=utf-8
family = ["papa", "mama", "son", "daughter"]
fruit = ["Apple", "Orange", "banana"]
count = [1, 2, 3, 4, 5]

for i in family:
    print "A family has a %s.\n" % i

for i in fruit:
    print "We can ear a fruit: %r.\n" % i

for i in count:
    print "Let count the amount of fruits."
    print "%d \n" % count[i-1]

real_family = []

print "how many people your family has?"
people = raw_input('How many people? >')

for i in range(0, int(people)):    
    print "input one of people in your family."
    real_family.append(raw_input('give me a name of your family member >'))

print "You have %d people in your family" % int(people)
print "Here they are: \n"
for i in range(0, int(people)):
    print "%s \n" % real_family[i]
