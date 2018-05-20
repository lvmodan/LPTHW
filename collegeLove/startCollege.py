#!/usr/bin/env python
# coding=utf-8
from gotoCollege import gotoCollege
from meetALovelyGirl import meetALovelyGirl
from collegeLoveFile import collegeLove

print """
A sunny day, you are go in your first college.
A bunch of people around you.
You are happy and curriocity.
Let's start the wonderful college life, a part of your life.
"""

walk = gotoCollege()
result = meetALovelyGirl(walk)
collegeLove(result)
