#!/usr/bin/env python
# coding=utf-8
from  scenes import *
from engine import engine
from map import map

amap = map('central_corridor')
aengine = engine(amap)
aengine.play()
