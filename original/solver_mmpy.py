#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input

import time
from Tkinter import *


def distance(ps):
    size = len(ps)
    table = [[0] * size for _ in xrange(size)]
    for i in xrange(size):
        for j in xrange(size):
            if i != j:
                dx = ps[i][0] - ps[j][0]
                dy = ps[i][1] - ps[j][1]
                table[i][j] = math.sqrt(dx * dx + dy * dy)
    return table

def memoize(f):
    table = {}
    def func(*args):
        if not args in table:
            table[args] = f(*args)
        return table[args]
    return func

def tsp(p, v):
    if (1 << point_size) - 1 == v:
        return distance_table[p][0]
    else:
        return min([distance_table[p][x] + tsp(x, v | (1 << x)) \
                    for x in xrange(point_size) if not (v & (1 << x))])

tsp = memoize(tsp)

def tsp_dp(size):
    size1 = size - 1
    table = [None] * (1 << size1)
    table[(1 << size1) - 1] = [distance_table[i][0] for i in xrange(1, size)]
    for v in xrange((1 << size1) - 2, 0, -1):
        tmp = [1e300] * size1
        for i in xrange(size1):
            if (1 << i) & v:
                tmp[i] = min([distance_table[i+1][j+1] + table[v | (1 << j)][j] \
                             for j in xrange(size1) if not (1 << j) & v])
        table[v] = tmp
    return min([distance_table[i+1][0] + table[1 << i][i] for i in xrange(size1)])


def min0(ary):
    v = (1e300, None)
    for x in ary:
        if v[0] > x[0]: v = x
    return v

def tsp_dp1(size):
    size1 = size - 1
    table = [None] * (1 << size1)
    table[(1 << size1) - 1] = [(distance_table[i][0], 0) for i in xrange(1, size)]
    for v in xrange((1 << size1) - 2, 0, -1):
        tmp = [1e300] * size1
        for i in xrange(size1):
            if (1 << i) & v:
                tmp[i] = min0([(distance_table[i+1][j+1] + table[v | (1 << j)][j][0], j) \
                               for j in xrange(size1) if not (1 << j) & v])
        table[v] = tmp
    s = min0([(distance_table[i+1][0] + table[1 << i][i][0], i) for i in xrange(size1)])
    return s[0], get_min_path(table, size, s[1])

def get_min_path(table, size, p):
    path = [0, p + 1]
    v = 1 << p
    while len(path) < size:
        _, q = table[v][p]
        path.append(q + 1)
        v |= (1 << q)
        p = q
    return path

point_table = read_input(sys.argv[1])
point_size = len(point_table)
distance_table = distance(point_table)

min_len, min_path = tsp_dp1(point_size)
#min_len = tsp_dp(point_size)
#min_path = []
print min_len
print_solution(min_path)
