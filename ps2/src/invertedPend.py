import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import rcParams
#rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

"""ex10.a"""
def DinvPend_a(var, t, alpha, k, c):
    x, y = var
    return [y - k*x + c, -alpha*y - np.sin(x)]
def invPend_a(ic, alpha, k, c):
    t = np.linspace(0, 15, 1001)
    states = odeint(DinvPend_a, ic, t, (alpha, k, c))
    return [t, states]
def invPendPlot_a(ic, alpha, k, c):
    t, states = invPend_a(ic, alpha, k, c)
    plt.plot(t, states[:, 0], label=r'$x(t)$')
    plt.plot(t, states[:, 1], label=r'$y(t)$')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$amplitude$')
    plt.xlim(t[0], t[-1])
    plt.legend(loc='best')
    plt.grid(True)

"""ex10.b"""
def DinvPend_b(var, t, alpha, k, c):
    x, y = var
    return [y, -alpha*y - np.sin(x) - k*x + c]
def invPend_b(ic, alpha, k, c):
    t = np.linspace(0, 30, 1001)
    states = odeint(DinvPend_b, ic, t, (alpha, k, c))
    return [t, states]
def invPendPlot_b(ic, alpha, k, c):
    t, states = invPend_b(ic, alpha, k, c)
    plt.plot(t, states[:, 0], label=r'$x(t)$')
    plt.plot(t, states[:, 1], label=r'$y(t)$')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$amplitude$')
    plt.xlim(t[0], t[-1])
    plt.legend(loc='best')
    plt.grid(True)

if __name__ == "__main__":
    """ex10.a"""
    c = lambda k: k*np.pi
    alpha = 0.3
    ic = [0, 0]
    k = 1/alpha
    #plt.figure(1); invPendPlot_a(ic, alpha, k, c(k))
    k = 2*(1/alpha)
    #plt.figure(2); invPendPlot_a(ic, alpha, k, c(k))
    k = 0.1*(1/alpha)
    #plt.figure(3); invPendPlot_a(ic, alpha, k, c(k))

    """ex10.b"""
    k = 0.9
    plt.figure(4); invPendPlot_b(ic, alpha, k, c(k))
    k = 4*(1 + alpha**2/4)
    plt.figure(5); invPendPlot_b(ic, alpha, k, c(k))
    k = 1 + alpha**2/4
    plt.figure(6); invPendPlot_b(ic, alpha, k, c(k))
    plt.show()
