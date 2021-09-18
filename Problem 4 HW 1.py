# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange,sin,cos
x = arange(-2*np.pi, 2*np.pi, 0.1)
plt.plot(x,sin(x), 'o-',x,cos(x),'^-')


plt.xlabel('value of x')
plt.ylabel('value of y')
plt.title('Sin x vs cos x on [-2pi,2pi]')
plt.legend(('sine','cosine'),loc = 0)
plt.grid(True)
plt.savefig('testplot.pdf',format='pdf')
plt.show()
input("\nPress return to exit")
