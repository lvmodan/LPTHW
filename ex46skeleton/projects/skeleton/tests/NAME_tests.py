#!/usr/bin/env python
# coding=utf-8
from nose.tools import *
import NAME

def setup():
    print 'setup'

def teardown():
    print 'teardown'

def test_basic():
    print 'I an running'
