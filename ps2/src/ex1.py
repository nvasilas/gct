import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import rcParams
#rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

"""ex10.a"""
def Dconv(var, t):
    x1, x2 = var
    return [x1**2 - x2**2, 2*x1*x2]
def conv(ic):
    t = np.linspace(0, 100, 1001)
    states = odeint(Dconv, ic, t)
    return [t, states]
def convPlot(ic):
    t, states = conv(ic)
    plt.figure(1)
    plt.plot(t, states[:, 0], label=r'$x_1(t)$')
    plt.plot(t, states[:, 1], label=r'$x_2(t)$')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$amplitude$')
    plt.legend(loc='best')
    plt.grid(True)

if __name__ == "__main__":
    ic = [10, 10]
    convPlot(ic)
    plt.show()
