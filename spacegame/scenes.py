#!/usr/bin/env python
# coding=utf-8

class scenes(object):
    
    def enter(self):
        print """
        every room is full of risk, watchout, venture.
        """

class central_corridor(scenes):
    def enter(self):
        print '''
        your ship is invaded by a bunch of gothon monster, you are the only one survival. 
        You are determined to end there monster.
        You need go to armory to get a neutraul bomb. and blow this ship with those gothon. finally, you can escape by escape_pod round the ship.
        you are in central_corridor now. this room is your beginning room. go adventure.
        There are 4 options you can explore:central_corridor, laser_weapon_armory, bridge, escape_pod
        look, a gothon is in the central_corridor, what do you want to do?
        shoot
        cry
        avoid touch
        fight by fist
        tempt it
        give a joke
        ...
        '''
        next = raw_input('go >')

        if next == 'shoot':
            print '''the gothon anger, it shoot you, you die.'''
            return 'death'
        elif next == 'cry':
            print '''the gothon look at you curiocity. then fight you'''
            return 'death'
        elif next == 'avoid touch':
            print '''the gothon found you. it shoot at you.'''
            return 'death'

        elif next == 'give a joke':
            print '''the gothon laugh to die. you can across its body, go to next room'''
            
            return 'laser_weapon_armory'
        else:
            print '''you are genuine. the gothon do not block you. you can go.'''
            return 'laser_weapon_armory'

class laser_weapon_armory(scenes):
    def enter(self):
        print '''laser_weapon_armory room. get bomb'''
        return 'bridge'

class bridge(scenes):
    def enter(self):
        print '''bridge room, place bomb'''
        return 'escape_pod'

class escape_pod(scenes):
    def enter(self):
        print '''escape pod. you get a new life.'''
        return 'central_corridor'

class death(scenes):
    def enter(self):
        print '''oh, you died. try again'''
        return 'central_corridor'
