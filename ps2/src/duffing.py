import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

"""ex2_a"""
def U(x):
    return -0.5*x**2 + 0.25*x**4
def yplus(x, h):
    return np.sqrt(2*h + x**2 - 0.5*x**4)
def yminus(x, h):
    return -np.sqrt(2*h + x**2 - 0.5*x**4)
def V(x, y):
    return 0.5*y**2 - 0.5*x**2 + 0.25*x**4 - 0.5

def undampedDuffingPlot():
    x0 = -2; xf = 2
    x = np.linspace(x0, xf, 100001)
    h = np.arange(-0.2, 1, 0.2)

    plt.figure(1)
    plt.plot(x, U(x), 'C0')
    plt.xlim(x0, xf)
    plt.ylabel(r'$U(x)$')
    plt.xlabel(r'$x$')
    plt.grid()
    #plt.savefig('ex2_undampedDuffingU.pdf')
    plt.figure(2)
    for i in range(0,len(h)):
        plt.plot(x, yplus(x, h[i]), 'C0', x, yminus(x, h[i]), 'C0')
    plt.xlim(x0, xf)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y(x)$')
    plt.grid(True)
    #plt.savefig('ex2_undampedDuffingPor.pdf')

"""ex2_b"""
def DdampedDuffing(var, t, zeta):
    x, y = var
    return [y, -zeta*y + x - x**3]

def dampedDuffing(zeta, ic):
    t = np.linspace(-100, 0, 1001)
    states = odeint(DdampedDuffing, ic, t, (zeta, ))
    return [t, states]

def dampedDuffingPlot(zeta, ic):
    t, states = dampedDuffing(zeta, ic)
    plt.figure(3)
    plt.plot(t, states[:, 0], label='$x(t), \zeta = ' + str(zeta) + '$')
    plt.plot(t, states[:, 1], label='$y(t), \zeta = ' + str(zeta) + '$')
    plt.legend(loc='best')
    plt.ylabel(r'$amplitude$')
    plt.xlabel('t')
    plt.grid(True)
    #plt.savefig('ex2_dampedDuffing.pdf')

def dampedDuffingPlotXY(zeta, ic):
    t, states = dampedDuffing(zeta, ic)
    plt.figure(4)
    plt.plot(states[:, 0], states[:, 1], 'C0')
    plt.xlabel(r'$x(t)$')
    plt.ylabel(r'$y(t)$')
    plt.legend(loc='best')
    plt.grid(True)
    #plt.savefig('ex2_attractors.pdf')

if __name__ == "__main__":
    undampedDuffingPlot()
    #dampedDuffingPlotXY(0.3, [-1.1, 0])
    #dampedDuffingPlot(0.3, [0.5, 0.5])
    #dampedDuffingPlot(0.7, [0.5, 0.5])
    #dampedDuffingPlot(np.sqrt(2)*2, [0.5, 0.5])
    plt.show()
