#!/usr/bin/env python
# coding=utf-8
from nose.tools import *
from game.game import Room

def setup():
    print 'setup'

def test_room():
    gold = Room('GoldRoom','''This room has a lot of gold, the only door is at north''')
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def teardown():
    print 'teardown'

def test_basic():
    print 'I an running'

def test_room_paths():
    center = Room('Center', 'Test room in the center.')
    north = Room('North', 'Test room in the north.')
    south = Room('South', 'Test room in the South.')

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room('Start', 'You can go west and down to hole.')
    west = Room('Trees', 'There are Trees here, you cam go east.')
    down = Room('Dungeon', 'It is dark down here, you can go up.')

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
