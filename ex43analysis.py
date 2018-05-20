#!/usr/bin/env python
# coding=utf-8
# thourouly testing is not possible
# early testing
# bug cluster
# 1 testing shows presense of defects (present defect, not prove perfect)
# 2 exhaustive testing is impossible
# 3 early testing (focus on defined objective)
# 4 defects clustering
# 5 pesticide paradox (imune, the testcase cannot find bugs)
# 6 testing is context dependent(e-commence, financial software, iot)
# 7 absence of error fallacy(perfect useless function is useless)
#
#Aliens
# invade
#space ship
#hero
#maze room
#escape pod
#planet
#game
#engine
#map
#scenes
# decription
#death
#central corridor
#laser weapon armory
#the bridge
#gothon
#
#map
 #-next scene
 #-opening scene
#class map(object):
#    scenes = {
#           'central_corridor': central_corridor(),
#        'laser_weapon_armory': laser_weapon_armory(),
#        'bridge': bridge(),
#        'escape_pod': escape_pod(),
#        'death': death()
#    }
#    def __init__(self, start_scene):
#        self.start_scene = start_scene
#
#    def next_scene(self, scene_name):
#        return map.scenes.get(scene_name)
#
#    def opening_scene(self, scene_name):
#        return map.next_scene(self.start_scene)

#engine
 #-play

class engine(object):
    def __init__(self, map_name):
        self.map_name = map_name

    def play(self):
        current_scene = self.map_name.openning_scene()
        while True:
            next_scene = current_scene.enter()
            current_scene = self.map_name.next_scene(next_scene)

#scenes
 #-enter
class scenes(object):
    def enter(self):
        pass
# death
# central corridor
# laser weapon armory
# the bridge
# escape pod
class death(scenes):
    def enter(self):
        pass

class central_corridor(scenes):
    def enter(self):
        print """
        You are in central_corridor, There is gothon wondering. watch out.
        where do you want to go?
        """
        action = raw_input('>')

        if action == 'shoot':
            print 'you kill the gothon'
            return 'escape_pod'
        else:
            print 'try again'
            return 'central_corridor'

class laser_weapon_armory(scenes):
    def enter(self):
        pass

class bridge(scenes):
    def enter(self):
        pass

class escape_pod(scenes):
    def enter(self):
        print 'you are in an escape_pod, you are survival.'
        return 'central_corridor'

class map(object):
    scenes = {
           'central_corridor': central_corridor(),
        'laser_weapon_armory': laser_weapon_armory(),
        'bridge': bridge(),
        'escape_pod': escape_pod(),
        'death': death()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return map.scenes.get(scene_name)

    def openning_scene(self):
        return map.next_scene(self.start_scene)
map = map('central_corridor')
engine = engine(map)
engine.play()

