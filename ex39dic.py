#!/usr/bin/env python
# coding=utf-8

state = {
    'California': 'CA',  
    'Michigan': 'MI',    
    'New York': 'NY',    
    'Florida': 'FL',    
    'Oregon': 'OR'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'NY': "New York",
    'FL': 'Jacksonville',
    'OR': 'Portland'
    }

def separatorline():
    print '>~~:>.o0 ' * 13

separatorline()
print 'state and abbreviare'

for s, abbr in state.items():
    print 'state > %s, abbreviate > %s' % (s, abbr)

for s, abbr in state.items():
    print 'state > %s, abbreviate > %s, contain cities: %s' % (s, abbr, cities[abbr])

separatorline()
err = state.get('Texas', None)

if not err:
    print 'Texas is working, can not find it.'

separatorline()

city = cities.get('TX', 'Does Not Exist')
print 'The city of  TX %s' % city 
