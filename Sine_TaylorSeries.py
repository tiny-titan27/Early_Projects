# This function has two inputs: Degree of accuracy (A) and x value in radians (R)
import sympy


def sine_taylor_series(a, r):
    x = sympy.Symbol('x')
    f = 0
    count = 1
    # The while loop determines the resulting series expansion. The r value is the input for x.
    while count < a+1:
        f = f + (-1) ** (count+1) * x ** (count*2-1) / sympy.factorial((count*2-1))
        count += 1
    f = f.subs(x, r)
    print(f)


sine_taylor_series(10, 1)
