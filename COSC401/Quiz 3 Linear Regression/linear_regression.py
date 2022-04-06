import numpy as np


def linear_regression(xs, ys):
    """
    Computes theta, an array of regression coefficients
    """
    xT = np.transpose(xs)
    xTx = np.matmul(xT, xs)
    xTx_inv = np.linalg.inv(xTx)
    xTy = np.matmul(xT, ys)
    theta = np.matmul(xTx_inv, xTy)
    return theta

xs = np.arange(5).reshape((-1, 1))
ys = np.arange(1, 11, 2)
print(linear_regression(xs, ys))

xs = np.array([[1, 2, 3, 4],
               [6, 2, 9, 1]]).T
ys = np.array([7, 5, 14, 8]).T
print(linear_regression(xs, ys))