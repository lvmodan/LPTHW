#!/usr/bin/env python
# coding=utf-8
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print 'Copying from %s to %s' % (from_file, to_file)

# try to so these two on one line too,

# in_file = open(from_file)
indata = (open(from_file)).read()

print 'The imput file is %d bytes long.' % len(indata)

print 'Dies the output file exists? %r' % exists(to_file)
print 'Ready, hit RETURN to continue, CTRL-C to abort.'
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print 'Alright, all done.'

out_file.close()
# in_file.close()
