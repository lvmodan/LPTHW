#!/usr/bin/env python
# coding=utf-8
class parent(object):
    def override(self):
        print 'parent function'

class child(parent):
    def override(self):
        print 'overrided, i an a child.'

dad = parent()
son = child()

dad.override()
son.override()
