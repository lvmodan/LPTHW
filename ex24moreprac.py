#!/usr/bin/env python
# coding=utf-8
print 'Let us practice everything.'
print "You\'d need to know \' about escapes with \\ that do \n newlines and \t tabs."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "---------------------"
print poem
print "----------------------"

five = 10 - 3 + 2 - 4
print 'This should be five: %s.' % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

started_point = 10000
beans, jars, crates = secret_formula(started_point)

print "With a starting point os : %d" % started_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

started_point /= 10

print "We can also do that this way."

print "We'd have %d beans, %d jars, and %d crates." % secret_formula(started_point)
