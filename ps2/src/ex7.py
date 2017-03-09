import numpy as np
from scipy.integrate import odeint
from scipy.linalg import expm
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

def Dsol(states, t, par):
    x, p = states
    a, b, q, r = par
    return [a*x - (b**2/r)*p, -q*x - a*p]

def sol(tspan, ic, par):
    t = np.linspace(tspan[0], tspan[1], 101)
    states = odeint(Dsol, ic, t, (par,))
    return [t, states]

def findp(tf, x0, par):
    a, b, q, r = par
    A = np.array([[a, -b**2/r], [-q, -a]])
    F = expm(A*tf)
    h = F[0, 0]
    j = F[0, 1]
    return -h/j*x0

def param(a = 2, b = 1, q = 1, r = 0.25):
    return (a, b, q, r)

def solPlot(tspan, ic, par):
    t, states = sol(tspan, ic, par)
    plt.figure(1)
    plt.plot(t, states[:, 0], label=r'$x^*(t)$')
    plt.plot(t, states[:, 1], label=r'$p^*(t)$')
    plt.plot(t, -par[2]/par[3]*states[:, 1], label=r'$u^*(t)$')
    plt.legend(loc='best')
    plt.ylabel(r'$amplitude$')
    plt.xlabel(r'$t$')
    plt.xlim(tspan[0], tspan[1])
    plt.grid(True)
    #plt.savefig('ex7_case1.pdf')

def case1():
    par = param()
    x0 = 5; tspan = (0, 3)
    p0 = findp(tspan[1], x0, par)
    ic = (x0, p0)
    solPlot(tspan, ic, par)
def case2():
    par = param(a = 5)
    x0 = 5; tspan = (0, 3)
    p0 = findp(tspan[1], x0, par)
    ic = (x0, p0)
    solPlot(tspan, ic, par)

if __name__ == "__main__":
    case1()
    case2()
    plt.show()
