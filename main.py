from sympy import *
x, xv = symbols("x xv", cls=Function)
t, x0, xv0 = symbols("t x0 xv0")
system = [Eq(x(t).diff(t), xv(t)), Eq(xv(t).diff(t),x(t))]
ics = {x(0): x0, xv(0): xv0}
res = dsolve(system, [x(t), xv(t)], ics=ics)
qq = 0