import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm, solve
from matplotlib import rcParams
#rcParams['font.family'] = "Linux Libertine O"
rcParams['text.usetex'] = True
rcParams['text.latex.unicode'] = True

def findM(M):
    a1, a2, a3 = M[0]
    b1, b2, b3 = M[1]
    c1, c2, c3 = M[2]
    l1 = -1
    l2 = -2
    l3 = -3
    det1 = (a1 - l1)*((b2 - l2)*(c3 - l3) - b3*c2)
    det2 = -a2*(b1*(c3 - l3) - b3*c1)
    det3 = a3*((b1*c2) - ((b2 - l2)*c1))
    return det1 + det2 + det3
M = np.array([[-1., 3., 3.], [0., -2., 0.], [0., 3., -3.]])
print(findM(M))
print("Eigenvalues of M are ", np.linalg.eig(M)[0])

Q = np.array([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]])
P = np.array([[2., -1., 1.], [-1., 2., -1.], [1., -1., 2.]])
print("Eigenvalues of Q are ", np.linalg.eig(Q)[0])
print("Eigenvalues of P are ", np.linalg.eig(P)[0])
A = solve(Q, -P)
print("Matrix A is ", A)
print("Eigenvalues of A are ", np.linalg.eig(A)[0])

t = np.linspace(0, 15, 1001)
x = np.zeros((3, len(t)))
x0 = [1., 2., 3.]
j = 0
for i in t:
    x[:, j] = expm(A*i).dot(x0)
    j += 1

print(x[0,-1], x[1,-1], x[2, -1])
plt.figure(1)
plt.plot(t, x[0,:], label='$x(t)$')
plt.plot(t, x[1,:], label='$y(t)$')
plt.plot(t, x[2,:], label='$z(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
