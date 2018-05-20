#!/usr/bin/env python
# coding=utf-8
print """
You are in a dark room. there are only two doors. which door you will choose to escape the room?
choose 1 or 2 to open the door.
"""

door = raw_input('which door? >')

if door == '1':
    print """
    You opened door1, there is a bear who is hungery and eating a cake. What do you decide to do?
    1: Attack the bear, and get the cake.
    2: Steal the cake.
    3: screaming...
    """
    decision = raw_input('input your decision >')
    if decision == '1':
        print """
        The bear anger, it beats u, and you are die.
        """

    elif decision == '2':
        print """
        The bear uncovered you, you are die.
        """

    elif decision == '3':
        print """
        You hurt the ear of bear. you get the cake. lucky.
        """

    else:
        print "You are make a meaningless decision: %s." % decision
    
elif door == '2':
    print """
    tThe door2 opened. there is a garden full of flowers.
    Do you want pick one flower.
    """
    flower = raw_input('pick or not >')
    if flower == 'yes' or flower == 'pick':
        print """
        A farmer apears, you should pay 1000 dollars as punish
        """
    elif flower == 'no' or flower == 'not':
        print """
        The peace make you happy. you get satisfied from the garden.
        """
    else:
        print """
        What are you talking about: %s ?
        """ % flower

else:
    print "You walk around and starve to die. To survive next life."
