# This function has two inputs: Degree of accuracy (A) and function to expand (r)
# This function is a general form of my scripts that produce taylor expansions of sine and cosine.
import sympy
x = sympy.Symbol('x')


def taylor_expansion(a, r):
    f = 0
    count = 0
    # The while loop determines the resulting series expansion.
    while count < a:
        f = f + r.subs(x, 0)/sympy.factorial(count)*x**count
        r = sympy.diff(r, x)
        count += 1
    print(f)


taylor_expansion(5, sympy.exp(1)**x)
