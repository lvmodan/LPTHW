#!/usr/bin/env python
# coding=utf-8
my_name = 'Lyndon'
my_age = 23 # it is true
my_height = 175 #cm
my_weight = 60 # KG
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He is %d cenimeter tall." % my_height
print "He is %d kilogram heavy." % my_weight
print "Actually that is fine."
print "He has got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." % my_teeth

# This line is trick, try to get it exactly right
print "If I add %d, %d, and %d  I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
