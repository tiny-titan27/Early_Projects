# This script describes the kinetics of a projectile launched
# There are four inputs: height of launch, initial velocity, angle of launch, and force gravity (defaults to 9.81)
# This script uses the sine and cosine scripts as references. For fun.

import sympy


def cosine_taylor_series(a, r):
    x = sympy.Symbol('x')
    f = 1
    count = 1
    # The while loop determines the resulting series expansion. The r value is the input for x.
    while count < a:
        f = f + (-1) ** count * x ** (count*2) / sympy.factorial((count*2))
        count += 1
    f = f.subs(x, r)
    return f


def sine_taylor_series(a, r):
    x = sympy.Symbol('x')
    f = 0
    count = 1
    # The while loop determines the resulting series expansion. The r value is the input for x.
    while count < a+1:
        f = f + (-1) ** (count+1) * x ** (count*2-1) / sympy.factorial((count*2-1))
        count += 1
    f = f.subs(x, r)
    return f


def projectile_motion(h, v_i, deg, g=9.81):
    rad = deg * 3.1415926/180
    v_x = cosine_taylor_series(5, rad) * v_i
    v_y = sine_taylor_series(5, rad) * v_i
    if h == 0:
        time_in_air = 2*v_y/g
    elif deg == 0:
        time_in_air = (2*h/9.81)**(1/2)
    else:
        time_in_air = (-v_y-(v_y**2+4*g/2*h)**(1/2))/(-g)
    distance_land = time_in_air * v_x
    max_height = (v_y/g)*v_y/2 + h
    print("The projectile spends ", time_in_air, "seconds in the air, and reaches a maximum height of ", max_height,
          "meters, landing ", distance_land, "meters away from the launch point.")


projectile_motion(30, 1000, 0)
