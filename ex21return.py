#!/usr/bin/env python
# coding=utf-8
def add(a, b):
    print "add %d and %d:" % (a, b)
    return a + b
def substract(a, b):
    print "minus %d and %d:" % (a, b)
    return a - b
def multiply(a, b):
    print "multiply %d and %d:" % (a, b)
    return a * b
def divide(a, b):
    print "%d divide %d:" % (a, b)
    return a / b

print "let's do some math:"
age = add(20, 3)
weight = substract(70, 5)
height = multiply(17, 10)
wist = divide(99, 2)

print "your age is %d, weight is %d, height is %d, wist is %d." % (age, weight, height, wist)

print "make thing more complicated;"
what = add(age, substract(height, multiply(weight, divide(wist, 2))))

print "what is %d" % what
