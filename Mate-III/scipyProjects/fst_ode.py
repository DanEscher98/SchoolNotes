#!/usr/bin/python
import math as mt
import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 5
a = -1/T
x0 = 1
t = 0
tstart = 0
tstop = 25
increment = 1

x = []
x = np.zeros(tstop+1)
t = np.arange(tstart, tstop+1, increment)

# Define equation
for k in range(tstop):
    x[k] = mt.exp(a*t[k]) * x0

print("hi")

# Plot the results
plt.plot(t, x)
plt.title('Ploting Differential Equation Solutions')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.axis([0, 25, 0, 1])
plt.savefig('anode.png')
plt.show()
