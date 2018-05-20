#!/usr/bin/env python
# coding=utf-8

from scenes import *
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
        return self.next_scene(self.start_scene)

