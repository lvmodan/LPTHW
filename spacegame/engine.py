#!/usr/bin/env python
# coding=utf-8
from map import *
class engine(object):

    def __init__(self, map_name):
        self.map_name = map_name

    def play(self):
        current_scene = self.map_name.openning_scene()
        while True:
            next_scene = current_scene.enter()
            current_scene = self.map_name.next_scene(next_scene)
