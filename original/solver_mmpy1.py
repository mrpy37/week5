
import sys
import math
import time
from Tkinter import *
from common import print_solution, read_input

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

def path_length(path):
    n = 0
    i = 1
    for i in xrange(1, len(path)):
        n += distance_table[path[i - 1]][path[i]]
    n += distance_table[path[0]][path[-1]]
    return n

def opt_2(size, path):
    global distance_table
    total = 0
    while True:
        count = 0
        for i in xrange(size - 2):
            i1 = i + 1
            for j in xrange(i + 2, size):
                if j == size - 1:
                    j1 = 0
                else:
                    j1 = j + 1
                if i != 0 or j1 != 0:
                    l1 = distance_table[path[i]][path[i1]]
                    l2 = distance_table[path[j]][path[j1]]
                    l3 = distance_table[path[i]][path[j]]
                    l4 = distance_table[path[i1]][path[j1]]
                    if l1 + l2 > l3 + l4:
                        new_path = path[i1:j+1]
                        path[i1:j+1] = new_path[::-1]
                        count += 1
        total += count
        if count == 0: break
    return path, total


def or_opt(size, path):
    global distance_table
    total = 0
    while True:
        count = 0
        for i in xrange(size):
            i0 = i - 1
            i1 = i + 1
            if i0 < 0: i0 = size - 1
            if i1 == size: i1 = 0
            for j in xrange(size):
                j1 = j + 1
                if j1 == size: j1 = 0
                if j != i and j1 != i:
                    l1 = distance_table[path[i0]][path[i]]  # i0 - i - i1
                    l2 = distance_table[path[i]][path[i1]]
                    l3 = distance_table[path[j]][path[j1]]  # j - j1
                    l4 = distance_table[path[i0]][path[i1]] # i0 - i1
                    l5 = distance_table[path[j]][path[i]]   # j - i - j1
                    l6 = distance_table[path[i]][path[j1]]
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        p = path[i]
                        path[i:i + 1] = []
                        if i < j:
                            path[j:j] = [p]
                        else:
                            path[j1:j1] = [p]
                        count += 1
        total += count
        if count == 0: break
    return path, total

def optimize1(size, path):
    while True:
        path, _ = opt_2(size, path)
        path, flag = or_opt(size, path)
        if flag == 0: return path

def optimize2(size, path):
    while True:
        path, _ = or_opt(size, path)
        path, flag = opt_2(size, path)
        if flag == 0: return path


def greedy0(path):
    size = len(path)
    for i in xrange(size - 1):
        min_len = 1e300
        min_pos = 0
        for j in xrange(i + 1, size):
            l = distance_table[path[i]][path[j]]
            if l < min_len:
                min_len = l
                min_pos = j
        path[i + 1], path[min_pos] = path[min_pos], path[i + 1]
    return path


def sign(x, y):
    if x == y: return 0
    if x < y: return -1
    return 1

def make_lower_value(size):
    table = []
    for i in xrange(size):
        tmp = [distance_table[i][j] for j in xrange(size)]
        tmp.sort()
        min_len = (tmp[1] + tmp[2]) / 2
        table.append(min_len)
    return table

def dfs(buff):
    def perm(n, size, path, now_len, rest_len):
        global min_len, min_path
        if now_len + rest_len > min_len:
            return
        if size == n:
            new_len = now_len + distance_table[path[-1]][path[0]]
            if new_len < min_len:
                min_len = new_len
                min_path = path[:]
        else:
            for x in xrange(1, size):
                if x not in path:
                    if n != 2 or path[0] < x:
                        new_len = now_len + distance_table[path[-1]][x]
                        path.append(x)
                        perm(n + 1, size, path, new_len, rest_len - lower_table[x])
                        path.pop()

    global min_len, min_path, lower_table
    lower_table = make_lower_value(point_size)

    min_path = optimize1(point_size, greedy0(range(point_size)))
    min_len = path_length(min_path)
    for x in xrange(1, point_size):
        perm(2, len(buff), [x, 0], distance_table[x][0], sum(lower_table[1:]))
    return min_path


point_table = read_input(sys.argv[1])
point_size = len(point_table)
distance_table = distance(point_table)

dfs(range(point_size))
print min_len
print_solution(min_path)
