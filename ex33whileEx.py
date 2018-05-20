#!/usr/bin/env python
# coding=utf-8

def fill_box():        
    n = int( raw_input('how many do you want to fill to box? >'))
    i = 0
    box = []
   
    print 'while loop starting...'
    while i in range(0, n):
        print 'in the while loop. %d ' %i
        print 'At the top, i = %d.' % i
        box.append(i)
        i += 1
        print "Now the box has:.",  box
    
    print "Now i = %d." % i 
    print "whileile loop envd. bye."
    
    for num in box:
        print "Here are things in box: %r\n" % num

fill_box()
