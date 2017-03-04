import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import rcParams
#rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

def U(x):
    return -np.cos(x)
def yplus(x, h):
    return np.sqrt(2*h + np.cos(x))
def yminus(x, h):
    return -np.sqrt(2*h + np.cos(x))

def undampedsimplePendulum():
    x0 = -1.5*np.pi; xf = 1.5*np.pi
    x = np.linspace(x0, xf, 100001)
    #h = np.arange(0, 0.5*np.sqrt(2), 0.1)
    h = [0, 0.3, 0.5, 0.7]

    plt.figure(1)
    plt.subplot(211)
    plt.plot(x, U(x), 'C0')
    plt.xlim(x0, xf)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$U(x)$')
    plt.grid()

    plt.subplot(212)
    for i in range(0,len(h)):
        plt.plot(x, yplus(x, h[i]), 'C0', x, yminus(x, h[i]), 'C0')
    plt.xlim(x0, xf)
    plt.xlabel(r'$x(t)$')
    plt.ylabel(r'$y(t)$')
    plt.grid()
    #plt.savefig('ps8_ex1a.png')

def DsimplePedulum(var, t, alpha):
    x, y = var
    return [y, -alpha*y - np.sin(x)]

def simplePedulum(alpha, ic):
    t = np.linspace(0, 50, 10001)
    statesPlus = odeint(DsimplePedulum, ic, t, (alpha, ))
    ic[1] *= -1
    statesMinus = odeint(DsimplePedulum, ic, t, (alpha, ))
    return [t, statesPlus, statesMinus]

def simplePedulumPlot(alpha, ic):
    t, statesPlus, statesMinus = simplePedulum(alpha, ic)
    plt.figure(4)
    plt.plot(t, statesPlus[:, 0], label='x(t)')
    plt.plot(t, statesPlus[:, 1], label='y(t)')
    plt.plot(t, statesMinus[:, 0], label='x(t)')
    plt.plot(t, statesMinus[:, 1], label='y(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()

def simplePedulumPlotXY(alpha, ic):
    t, statesPlus, statesMinus = simplePedulum(alpha, ic)
    plt.figure(5)
    plt.plot(statesPlus[:, 0], statesPlus[:, 1], 'C0')
    plt.plot(statesMinus[:, 0], statesMinus[:, 1], 'C0')
    plt.xlim(-2.1*np.pi, 2.1*np.pi)
    plt.ylim(-3.5, 3.5)
    plt.xlabel(r'$x(t)$')
    plt.ylabel(r'$y(t)$')
    plt.grid(True)

def dampedVectorField(alpha):
    x0 = -2*np.pi; xf = 2*np.pi
    y0 = -3; yf = 3
    x = np.arange(x0, xf, .5)
    y = np.arange(y0, yf, .5)
    X, Y = np.meshgrid(x, y)
    DX = Y
    DY = -alpha*Y - np.sin(X)

    plt.figure(6)
    plt.streamplot(X, Y, DX, DY)
    plt.xlabel(r'$x(t)$')
    plt.ylabel(r'$y(t)$')
    plt.grid()

def phase_plot(alpha):
    ic = [[0, 0.2], [0, 1], [-2*np.pi, 0.2],\
            [-2*np.pi, 1], [2*np.pi, 0.2], [-2*np.pi, 1],\
            [2*np.pi, 0.2], [2*np.pi, 1], [0, 2],\
            [2*np.pi, -2], [2*np.pi, 2], [-2*np.pi, -2],\
            [-2*np.pi, 2], [0, -2], [0, 2.5],\
            [0, -2.5], [0, 3], [0, -3]]
    for i in ic:
        simplePedulumPlotXY(alpha, i)

alpha = -0.5
phase_plot(alpha)
plt.show()
