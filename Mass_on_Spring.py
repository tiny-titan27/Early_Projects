# This script outputs a graph showing the position of a mass hanging from a vertical spring

import sympy
x = sympy.Symbol('x')
t = sympy.Symbol('t')


def mass_on_spring_y(h, k, m):
    w = (k/m)**1/2
    y = h * sympy.cos(w*t)
    T = 2*sympy.pi/w
    print("The oscillations have a period of ", T, "seconds.")
    sympy.plotting.plot(y, (t, 0, 2*T))


mass_on_spring_y(5, 1, 3)


def mass_on_spring_v(h, k, m):
    w = (k / m) ** 1 / 2
    T = 2 * sympy.pi / w
    v = -w * h * sympy.sin(w * t)
    print("The mass has a maximum velocity of ", w*h, "meters per second.")
    sympy.plotting.plot(v, (t, 0, 2 * T))


def mass_on_spring_a(h, k, m):
    w = (k / m) ** 1 / 2
    y = h * sympy.cos(w * t)
    T = 2 * sympy.pi / w
    a = -w ** 2 * h * sympy.cos(w * t)
    print("The mass has a maximum acceleration of ", w**2*h, "seconds.")
    sympy.plotting.plot(a, (t, 0, 2 * T))
