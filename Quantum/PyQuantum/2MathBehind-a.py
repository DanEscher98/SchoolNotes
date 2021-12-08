#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 18:08:32 2021

@author: dany98
"""

import numpy
import scipy
import scipy.linalg

def multi_quantum_state(*args):
    ret = numpy.array([[1]])
    for q in args:
        ret = numpy.kron(ret, q)
    return ret
    
sOne = numpy.array([[0], [1]])
sZero = numpy.array([[1], [0]])
H = 1/numpy.sqrt(2)*numpy.array([[1, 1], [1, -1]])
I = numpy.eye(2)

new_QtmState = numpy.dot(H, sZero)

SWAP = numpy.array([[1,0,0,0],
                    [0,0,1,0],
                    [0,1,0,0],
                    [0,0,0,1]])

NormalizeQtmState = lambda qtmstate: qtmstate/scipy.linalg.norm(qtmstate) 

t0_QtmState = multi_quantum_state(sZero, sOne)
t1_QtmState = numpy.dot(SWAP, t0_QtmState)
t2_QtmState = numpy.dot(multi_quantum_state(H, I), t0_QtmState)