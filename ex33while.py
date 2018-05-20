#!/usr/bin/env python
# coding=utf-8
i = 0
box = []

while i < 6:
    print 'At the top, i = %d.' % i
    box.append(i)
    i += 1
    print "Now the box has:.",  box

print "Now i = %d." % i

for num in box:
    print "Here are things in box: %r\n" % num

