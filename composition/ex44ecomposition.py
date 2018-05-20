#!/usr/bin/env python
# coding=utf-8
class other(object):
    def implicity(self):
        print 'other implicity'

    def override(self):
        print 'other override'

    def alter(self):
        print 'other alter'

class person(object):
    def __init__(self):
        self.comp = other()

    def implicity(self):
        self.comp.implicity()

    def override(self):
        print 'person override'

    def alter(self):
        print 'before'
        self.comp.alter()
        print 'after'

person = person()

person.implicity()
person.override()
person.alter()
