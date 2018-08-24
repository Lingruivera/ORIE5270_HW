import numpy as np
import scipy as sc
from scipy import optimize


def RosenBrockFun(x):
    """
    compute the Rosenbrock function
    :param x: a n-dimensional array
    :return: value of the function
    """
    Sum = 0
    for i in range(len(x)-1):
        Sum = Sum + 100.0 * (x[i+1] - x[i] ** 2.0) ** 2.0 + (1 - x[i]) ** 2.0
    return Sum


def RosenBrockDer(x):
    """
    compute the derivative of the Rosenbrock function
    :param x: a 3-dimensional array
    :return: derivative at each dimension of the function
    """
    der = np.zeros(len(x))
    der[0] = -400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0])
    der[1] = 200 * (x[1] - x[0] ** 2) - 400 * (x[2] - x[1] ** 2) * x[1] - 2 * (1 - x[1])
    der[-1] = 200 * (x[-1] - x[-2] ** 2)
    return der


if __name__ == '__main__':
    x1 = np.arange(-5, 5.1, 0.5)
    x2 = np.arange(-5, 5.1, 0.5)
    x3 = np.arange(-5, 5.1, 0.5)
    X1, X2, X3 = np.meshgrid(x1, x2, x3)
    x = np.array([X1.flatten(), X2.flatten(), X3.flatten()]).T

    result = []
    obj_value = []
    for i in range(len(x)):
        x0 = x[i]
        res = sc.optimize.minimize(RosenBrockFun, x0, method='BFGS', jac=RosenBrockDer, options={'disp': False})
        result.append(res)
        obj_value.append(res.fun)

    result = result[np.argmin(obj_value)]
    print(result)
