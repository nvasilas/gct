import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True
rcParams['mathtext.fontset'] = 'cm'
rcParams['mathtext.rm'] = 'serif'

def checkPoint(a, b):
    tx = (2*b - a)/3
    ty = (2*a - b)/3
    if tx >= -0.5 and tx <= 0.5 and ty >= -0.5 and ty <= 0.5:
        print("point (a, b) = (",a,',', b,")___tx =",tx,"ty =",ty)
    else:
        print("NOT point (a, b) = (",a,',', b,")___tx =",tx,"ty =",ty)

def plotPoints():
    t = np.arange(-1, 1, 0.05)
    plt.figure(3)
    for i in t:
        for j in t:
            tx = (2*j - i)/3
            ty = (2*i - j)/3
            if tx >= -0.5 and tx <= 0.5 and ty >= -0.5 and ty <= 0.5:
                plt.plot(i, j, 'C3o')

def rhombus1Plot():
    plt.figure(1)
    """ plot lines ([x_old, x_new], [y_old, y_new]) """
    plt.plot([-1, -1], [-0.5, 1], 'C0')
    plt.plot([-1, 0.5], [1, 1], 'C0')
    plt.plot([1, 1], [0.5, -1], 'C0')
    plt.plot([1, -0.5], [-1, -1], 'C0')

    """ plot rhombus """
    plt.plot([0.5, 1], [1, 1], 'C1--')
    plt.plot([1, 1], [1, 0.5], 'C1--')
    plt.plot([1, 0.5], [0.5, -0.5], 'C1--')
    plt.plot([0.5, -0.5], [-0.5, -1], 'C1--')
    plt.plot([-0.5, -1], [-1, -1], 'C1--')
    plt.plot([-1, -1], [-1, -0.5], 'C1--')
    plt.plot([-1, -0.5], [-0.5, 0.5], 'C1--')
    plt.plot([-0.5, 0.5], [0.5, 1], 'C1--')

    """ plot axes """
    plt.plot([0, 0], [-1, 1], 'C7--')
    plt.plot([-1, 1], [0, 0], 'C7--')
    plt.grid(True)
    #plt.savefig('ex8_rhombus1.pdf')

def rhombus2Plot():
    plt.figure(2)
    """ plot lines ([x_old, x_new], [y_old, y_new]) """
    plt.plot([-1, -1], [-0.5, 0], 'C0')
    plt.plot([-1, -1], [0.25, 1], 'C0')
    plt.plot([-1, -0.25], [1, 1], 'C0')
    plt.plot([0, 0.5], [1, 1], 'C0')
    plt.plot([1, 1], [0.5, -1], 'C0')
    plt.plot([1, -0.5], [-1, -1], 'C0')

    """ plot rhombus """
    plt.plot([0.5, 1], [1, 1], 'C1--', label=r'$n = 1$')
    plt.plot([1, 1], [1, 0.5], 'C1--')
    plt.plot([1, 0.5], [0.5, -0.5], 'C1--')
    plt.plot([0.5, -0.5], [-0.5, -1], 'C1--')
    plt.plot([-0.5, -1], [-1, -1], 'C1--')
    plt.plot([-1, -1], [-1, -0.5], 'C1--')
    plt.plot([-1, -0.5], [-0.5, 0.5], 'C1--')
    plt.plot([-0.5, 0.5], [0.5, 1], 'C1--')

    """ plot rhombus at new point
    with center (-0.5, 0.5) """
    plt.plot([-0.25, 0], [1, 1], 'C2--', label=r'$n = 2$')
    plt.plot([0, 0], [1, 0.75], 'C2--')
    plt.plot([0, -0.25], [0.75, 0.25], 'C2--')
    plt.plot([-0.25, -0.75], [0.25, 0], 'C2--')
    plt.plot([-0.75, -1], [0, 0], 'C2--')
    plt.plot([-1, -1], [0, 0.25], 'C2--')
    plt.plot([-1, -0.75], [0.25, 0.75], 'C2--')
    plt.plot([-0.75, -0.25], [0.75, 1], 'C2--')

    """ plot axes """
    plt.plot([0, 0], [-1, 0.75], 'C7--')
    plt.plot([-0.75, 1], [0, 0], 'C7--')

    plt.plot([-0.5, -0.5], [0, 1], 'C7--')
    plt.plot([-1, 0], [0.5, 0.5], 'C7--')
    plt.grid(True)
    plt.legend(loc='upper right')
    #plt.savefig('ex8_rhombus2.pdf')

if __name__ == "__main__":
    #rhombus1Plot()
    rhombus2Plot()
    #plotPoints()
    checkPoint(0, 0.75)
    plt.show()
