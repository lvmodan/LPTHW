#!/usr/bin/env python
# coding=utf-8
def cheese_and_crackers(cheese_count, cracker_count):
    print "you have %r cheese." % cheese_count
    print "you have %s cracker." % cracker_count
    print "It is enough for our party."
    print "Get a blanket. \n"

print "We can just put some number in the function. let's do it."
cheese_and_crackers(3,6)

print "We can declare some variable, and pass them on the function. let's go..."
cheese_count = 33
cracker_count = 66
cheese_and_crackers(cheese_count, cracker_count)

print "We can do some math in the function. try it."
cheese_and_crackers(3+6, 6+9)

print "We can combine the variable and number and math. crazyly go..."
cheese_and_crackers(cheese_count+3, cracker_count+6)
