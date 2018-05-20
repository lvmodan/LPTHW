#!/usr/bin/env python
# coding=utf-8
def print_two(* args):
    arg1, arg2 = args
    print "arsterisk args: arg1 %r, arg2 %r." % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "two parameter in function brackets: arg1 %r, arg2 %r." % (arg1, arg2)

def print_one(arg1):
    print "one parameter: arg1 %r." % arg1

def print_none():
    print "No parameter in this function."

print_two('hi', 'python')
print_two_again('hello', 'homo')
print_one('sapines')
print_none()
