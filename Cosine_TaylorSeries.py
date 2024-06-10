# This function has two inputs: Degree of accuracy (A) and x value in radians (R)
import sympy


def cosine_taylor_series(a, r):
    x = sympy.Symbol('x')
    f = 1
    count = 1
    # The while loop determines the resulting series expansion. The r value is the input for x.
    while count < a:
        f = f + (-1) ** (count) * x ** (count*2) / sympy.factorial((count*2))
        count += 1
    f = f.subs(x, r)
    return(f)


cosine_taylor_series(4, 1)
