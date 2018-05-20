#!/usr/bin/env python
# coding=utf-8
class parent(object):
    def alter(self):
        print 'parent alter function'

class child(parent):
    def alter(self):
        print 'I am a child'
        super(child, self).alter()
        print 'used super'

dad = parent()
son = child()

dad.alter()
son.alter()
