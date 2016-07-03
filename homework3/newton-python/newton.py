import numpy as np


def solve(fvals, x0, debug=False):
    """
    This function implements the Newton's method in Python
    Inputs:
        * fvals, a function that returns the values of f(x) and
                 f'(x) for any input x.
        * x0, the initial guess.
        * debug, an optional argument with default False. 
    Outputs:
        * approximation of the final iterate.
        * the number of iterations taken.
    """
    maxiter = 20
    tol = 1e-14
    
    # Initial guess
    x = x0

    if debug:
        print('Initial guess: x = %20.15e' % x)

    # Newton iteration to find a zero of f(x)

    for i in range(0, maxiter):
        # Evaluate function and its derivative
        fx, fxprime = fvals(x)
        if (abs(fx) < tol):
            break

        # Compute Newton increment x
        deltax = fx / fxprime

        # Update x
        x = x - deltax

        if debug:
            print('After %d iterations, x = %20.15f' % (i, x))

    if (i > maxiter):
        # Might not have converged
        fx = fvalues(x)[0]

        if (abs(fx > tol)):
            print('*** Warning: has not yet converged')

    iters = i - 1

    return x, iters

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2. * x

    return f, fp


def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    condicitions.
    """
    for x0 in [1., 2., 100.]:
        print(' ')
        x, iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print('Solve returns x = %22.15e after %i iterations' % (x, iters))
        fx, fpx = fvals_sqrt(x)
        print('The value of f(x) is %22.15e' % fx)
        assert abs(x - 2.) < 1e-14, '*** Unexpected result: x = %22.15e' % x

        
