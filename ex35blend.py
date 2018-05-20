#!/usr/bin/env python
# coding=utf-8

def start():
    print 'You are in a dark room.'
    print 'There is a door to yout right and left'
    print 'Which door do you take?'

    next = raw_input("left or right? > ")

    if next == 'left':
        bear_room()
    elif next == 'right':
        cthulhu_room()
    else:
        dead('You stumble around the room until you starve.')

def bear_room():
    print """
    There is a bear here, it is huge and horriable.
    The bear occupy a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    """

    bear_moved = False

    while True:
        next = raw_input('How do you do? 1 take honey, 2 taunt bear, 3 open door >')

        if next == 'take honey':
            dead('The bear looks at you then slaps your face off')
        elif next == 'taunt bear' and not bear_moved:
            print 'The bear has moved from the door. You can go through it now.'
            bear_moved = True
        elif next == 'taunt bear' and bear_moved:
            dead('Bear anger at you, crying at you.')
        elif next == 'open door' and bear_moved:
            gold_room()
        else:
            print 'What are you talking about?'


def cthulhu_room():
    print """
    Here is a great evil Cthulhu.
    if he stare at you, you will be insane.
    Do you flee for your life or close your eye?
    """

    decision = raw_input('flee or close? >')

    if "flee" in decision:
        start()
    elif "close" in decision:
        dead('You lost the time, and starve')
    else:
        cthulhu_room()

def gold_room():
    print """ 
    Here are full of gold, how many gold could you want to take?
    """

    gold = raw_input('How many gold you want to take? >')

#    if 0 in gold or '1' in gold:"
    if gold in "0123456789":
        count = int(gold)
    else:
        dead('Type a number')

    if count < 50:
        print "Nice, you are rich now. good luck."
        exit(0)
    else:
        dead('Too much gold has killed you')

def dead(why):
    print why, 'Try to survive next life.'
    exit(0)

start()
