import numpy as np
from newton import solve
import matplotlib.pyplot as plt

def fvals_func(x):
    """
    Returs a tuple with f(x) and f'(x) where f(x) is equal to:
    f(x) = sin(x) - 1 + x**2
    """
    g1 = x * np.cos(np.pi * x)
    g2 = 1 - 0.6 * x**2
    fx = g1 - g2
    fxprima = np.cos(np.pi * x) - np.pi * x * np.sin(np.pi * x) + 1.2 * x 

    return fx, fxprima


def print_intersections(fvals_func):
    for x0 in [-2.20, -1.5, -0.7, 1.5]: # x0 taken looking at the plot
        x, iters = solve(fvals_func, x0)
        print('With initial guess x0 %20.15e,\n      solve returns x = %20.15e after %i iterations' % (x0, x, iters))
    

def plot_intersections(fvals_func):
    x = np.linspace(-5, 5, 300)
    
    xx = np.empty(4)
    for i, x0 in enumerate([-2.20, -1.5, -0.7, 1.5]):
        xx[i], iters = solve(fvals_func, x0)
    yy = 1 - 0.6 * xx**2

    fig, ax = plt.subplots()
    ax.plot(x, x * np.cos(np.pi * x), 'r', label='$g_{1}(x)=sin(x)$')
    ax.plot(x, 1 - 0.6 * x**2, 'b', label='$g_{2}(x)=1-x^2$')
    ax.plot(xx, yy, 'ko', label='intersections')

    ax.set_xlim(-5, 5)
    ax.legend(loc='lower left')

    fig.savefig('intersections.png')


    
