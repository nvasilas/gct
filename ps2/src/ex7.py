import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from scipy.linalg import expm, solve
from matplotlib import rcParams
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

def x_star(t, par, ic):
    a, b, q, r, w, v = par
    c1, c2 = ic
    state = np.sqrt(r)*w*c2*np.cosh(v*t)
    state += (b**2*c1 + a*r*c2)*np.sinh(v*t)
    state /= np.sqrt(r)/w
    return state
def p_star(t, par, ic):
    a, b, q, r, w, v = par
    c1, c2 = ic
    state = w*c1*np.cosh(v*t)
    state -= np.sqrt(r)*(a*c1 + q*c2)*np.sinh(v*t)
    state /= w
    return state
def u_star(t, par, ic):
    p = p_star(t, par, ic)
    return -par[1]*p/par[3]
def findInit(y, t, par, ic):
    return (ic[0] - x_star(t, par, y), \
            ic[1] - p_star(t, par, y))

a = 2
b = 5
q = 1
r = 0.5
par = [a, b, q, r]
w = np.sqrt(b**2*q + a**2*r)
v = np.sqrt((b**2*q + a**2*r)/r)
par.append(w)
par.append(v)

ic = [0, 0]
t = np.linspace(0, 10, 101)
x = np.zeros((2, len(t)))
j = 0
A = np.array([[a, -b**2/r], [-q, -a]])
for i in t:
    x[:, j] = expm(A*i).dot(ic)
    j += 1
u = -b/r*x[1,:]

plt.figure(1)
plt.plot(t, x[0,:], label='$x(t)$')
plt.plot(t, x[1,:], label='$p(t)$')
plt.plot(t, u, label='$u(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
