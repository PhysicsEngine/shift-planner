#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  i: arbeit_i N
#  j: day      7
#  k: time     3
#
#  S_ijk: Satisfaction of member i join at day j and k.
#  x_ijk: 1 or 0
#
#  Conditions:
#  sum x_ijk > 3
#   i
#

import numpy as np
import pulp

N = 5
D = 7
T = 2

S = np.random.rand(N, D, T) - 0.5

var = pulp.LpVariable.dicts('VAR', (range(N), range(D), range(T)), 0, 1, 'Binary')

obj = None
for i in range(N):
    for j in range(D):
        for k in range(T):
            obj += S[i][j][k] * var[i][j][k]

problem = pulp.LpProblem('shift', pulp.LpMaximize)

problem += obj

for j in range(D):
    for k in range(T):
        c = None
        for i in range(N):
            c += var[i][j][k]
        problem += c >= 3

print problem

status = problem.solve()
print "Status", pulp.LpStatus[status]

print "----------"
print "Result"
for i in range(N):
    print "Member{}".format(i)
    for j in range(D):
        print "{}day".format(j),
        for k in range(T):
            status = "NO"
            if var[i][j][k].value() > 0.0:
                status = "OK"
            print "Time{} => {},".format(k, status),
        print ""
    print ""

