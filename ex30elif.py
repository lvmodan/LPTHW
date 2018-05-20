#!/usr/bin/env python
# coding=utf-8
people = 30
cars = 20
buses = 10

if people > cars:
    print "We can not drive cars."
elif people > cars:
    print "We can not2 drive cars."
elif people < cars:
    print "We can drive cars."
else:
    print "We do not know."

if buses > cars:
    print "There are more buses than cars."
elif buses < cars:
    print "We can take the buses."
else:
    print "We still can not decide."

if people > buses:
    print "Let us take the buses."
else:
    print "no more decision, just stay home."
