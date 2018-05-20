#!/usr/bin/env python
# coding=utf-8
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(2)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print 'First, let us print_all:'
print_all(current_file)

print 'Secondly, let us rewind the file:'
rewind(current_file)

print 'Finally, let us read the file by line:'
print 'line 1:'
current_line = 1
print_a_line(current_line, current_file)

print 'line 2: '
current_line += 1
print_a_line(current_line, current_file)

print 'line 3: '
current_line += 1
print_a_line(current_line, current_file)
