#!/usr/bin/env python
# coding=utf-8
class parent(object):
    def implicit(self):
        print 'parent function'

class child(parent):
    pass

dad = parent()
son = child()

dad.implicit()
son.implicit()
