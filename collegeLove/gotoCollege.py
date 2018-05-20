#!/usr/bin/env python
# coding=utf-8

def gotoCollege():
    print """
    Beautiful biulding, so nice place.
    You must get a wonderful college life.
    """
    
    walkAround = raw_input('Do you like to walkAround the college? >')
    
    if walkAround == 'yes':
        print """
        you walk around the college.
        many people pass bt you.
        You are interesting on the people.
        """
    else:
        print """
        You are going to apartment.
        You want to have a rest.
        """
    
    return walkAround
