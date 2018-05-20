#!/usr/bin/env python
# coding=utf-8
sentence = 'I like that girl and crash on her'
senlist = sentence.split(' ')
moreSrc = ['love', 'life', 'family' ]

while len(senlist) < 10:
    addThis = moreSrc.pop()
    print 'We will welcome this source: ', addThis
    senlist.append(addThis)
    print 'Now the length is : %i' % len(senlist)

print 'What is more'

print "-->".join(senlist)
print " ". join(senlist[3: 7])

