import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

def checkPoint(a, b):
    tx = (2*b - a)/3
    ty = (2*a - b)/3
    if tx >= -1 and tx <= 1 and ty >= -1 and ty <= 1:
        print("point (a, b) = (",a,',', b,")___tx =",tx,"ty =",ty)

def rhombusPlot():
    plt.figure(1)
    """ plot lines"""
    plt.plot([-1, 0.5], [1, 1], 'C0')
    plt.plot([-1, -1], [-0.5, 1], 'C0')
    plt.plot([1, 1], [0.5, -1], 'C0')
    plt.plot([-0.5, 1], [-1, -1], 'C0')

    """ plot rhombus"""
    plt.plot([-1, -0.5], [-0.5, 0.5], 'C1')
    plt.plot([-0.5, 0.5], [0.5, 1], 'C1')
    plt.plot([-0.5, 0.5], [-1, -0.5], 'C1')
    plt.plot([0.5, 1], [-0.5, 0.5], 'C1')

    """ plot missing lines"""
    plt.plot([0.5, 1], [1, 1], 'C1')
    plt.plot([1, 1], [1, 0.5], 'C1')
    plt.plot([-0.5, -1], [-1, -1], 'C1')
    plt.plot([-1, -1], [-1, -0.5], 'C1')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    checkPoint(0, -1)
