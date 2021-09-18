# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:19:23 2021

@author: Dglau
"""
import math
import numpy
import numpy as np 
from numpy import *
with open('input.txt', 'r') as myfile:
    L1=[]
    L2=[]
    for line in myfile:
        L1.append(eval(line.split()[0]))
        L2.append(eval(line.split()[1]))
myfile.close()


L1=numpy.array(L1)
L2=numpy.array(L2)
L3 =numpy.sqrt(L1)
L4=numpy.power(L2, 10.0)
print(L1,type(L1))
print(L2,type(L2))

with open('output.txt','w') as myfile:
    for k in range(0,len(L1)):
        myfile.write('{:1} {:1} {:10.9} {:10.4e}'.format(L1[k],L2[k],L3[k],L4[k]))
        myfile.write('\n')
myfile.close