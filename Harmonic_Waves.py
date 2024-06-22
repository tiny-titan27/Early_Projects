# This function will graph a harmonic wave
import sympy
x = sympy.Symbol('x')
t = sympy.Symbol('t')


def harmonic_wave(a, k, w, phi=0):
    f_x = a*sympy.cos(k*x+phi)
    f_t = a*sympy.cos(-w*t+phi)
    sympy.plotting.plot(f_x, (x, 0, (-phi+2*sympy.pi)/k))
    sympy.plotting.plot(f_t, (t, 0, (phi+2*sympy.pi) / k))


harmonic_wave(1, 2, 5)
