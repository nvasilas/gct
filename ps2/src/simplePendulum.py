import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import rcParams
#rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

def DsimplePedulum(var, t, alpha, T):
    x, y = var
    return [y, -alpha*y - np.sin(x) + T]

def simplePedulum(alpha, T, ic):
    t = np.linspace(0, 50, 101)
    states = odeint(DsimplePedulum, ic, t, (alpha, T))
    return [t, states]

def simplePedulumPlot(alpha, T, ic):
    t, states = simplePedulum(alpha, T, ic)
    plt.figure(1)
    xlabel = '$x(t), a = ' + str(alpha) + ', T = ' + str(T) + '$'
    ylabel = '$y(t), a = ' + str(alpha) + ', T = ' + str(T) + '$'
    plt.plot(t, states[:, 0], label=xlabel)
    plt.plot(t, states[:, 1], label=ylabel)
    plt.legend(loc='best')
    plt.ylabel(r'$amplitude$')
    plt.xlabel(r'$t$')
    plt.grid(True)

def equilibriumPerTorque(k = 0):
    x1 = lambda T, k: 2*k*np.pi + np.arcsin(T)
    x2 = lambda T, k: (2*k + 1)*np.pi - np.arcsin(T)
    print("for T = 0.5, x1 =", x1(0.5, k),"and x2 =",x2(0.5, k))
    print("for T = 0.7, x1 =", x1(0.7, k),"and x2 =",x2(0.7, k))
    T = np.linspace(0, 1, 1001)
    plt.figure(2)
    plt.plot(T, x1(T, k), label=r'$x_1(T)$')
    plt.plot(T, x2(T, k), label=r'$x_2(T)$')
    plt.legend(loc='best')
    plt.ylabel(r'$equilibirum$')
    plt.xlabel(r'$T$')
    plt.xlim(T[0], 1.1)
    plt.grid(True)
    #plt.savefig('ex4_equilibriumPerTorque.pdf')


if __name__ == "__main__":
    simplePedulumPlot(0.1, 0, [0.5, 0.5])
    #equilibriumPerTorque()
    plt.show()
