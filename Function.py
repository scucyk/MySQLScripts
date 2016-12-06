#!/usr/bin/env python
# coding:utf-8

"""This is the function module"""

__author__ = 'scucyk'


def compute(x, y):
    print 'call the outer function'

    def inner(r):
        print 'call the inner function'
        return r * x + y
    return inner
