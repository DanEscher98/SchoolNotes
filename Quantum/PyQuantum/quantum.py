import math
import numpy as np

class qState:
    def __init__(self, m, n):
        self.theta = m
        self.psi = n
        self.const = self._c(self.theta, self.psi)
    def __str__(self):
    	return "({}  {})".format(self.theta, self.psi)
    def __add__(self, other):
    	a = self.theta+other.theta
    	b = self.psi+other.psi
    	return qState(a, b)
    def __mul__(self, other):
    	c = self.const*other.const
    	a = self.theta*self.theta
    	b = self.psi*self.psi
    	ans = c*(a+b)
    	a = round(ans.real, 4)
    	b = round(ans.imag, 4)
    	return a+b*1j
    def _c(self, a, b):
        ans = csqrt(a**2 + b**2)[0]
        ans = 1/ans
        a = round(ans.real, 4)
        b = round(ans.imag, 4)
        return a+b*1j

def p2C(r, theta): #polar to cartesian complex
    ans = math.cos(theta) + math.sin(theta)*1j
    return ans*r

def c2P(z):
    r = math.sqrt(z.real**2 + z.imag**2)
    theta = math.atan2(z.imag, z.real)
    r = round(r, 4)
    theta = round(theta, 4)
    return (r, theta)

def csqrt(z):
    r = math.sqrt(z.real**2 + z.imag**2)
    theta = math.atan2(z.imag, z.real)
    ans = []
    for k in range(2):
        arg = (theta + 2*np.pi*k)/2
        absv = math.sqrt(r)
        a = (absv*math.cos(arg))
        b = (absv*math.sin(arg))
        ans.append((a+b*1j))
    return ans

if __name__ == '__main__':
    a = qState(1, 1)
    b = qState(1, 0)
    print("|a⟩ = {}".format(a))
    print("⟨a|b⟩ = {}".format(a*b))
    print(a+b)
    print((a+b)*b)
    print(a.const)