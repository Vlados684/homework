from sympy import *

"""
x = (a / (b + pow(c, 1/2))
av = 0.171
bv = 0.91
cv = 1.1
a_delta = 0.004
b_delta = 0.007
c_delta = 0.01
"""

a = Symbol("a")
b = Symbol("b")
c = Symbol("c")

x = eval(str(a / (b + pow(c, 1/2))))
av = float(0.171)
a_delta = float(0.004)
bv = float(0.91)
b_delta = float(0.007)
cv = float(1.1)
c_delta = float(0.01)


delta_a = x.diff(a)
delta_b = x.diff(b)
delta_c = x.diff(c)

a_delta = abs(delta_a.subs({a:av, b:bv, c:cv}))
b_delta = abs(delta_b.subs({a:av, b:bv, c:cv}))
c_delta = abs(delta_c.subs({a:av, b:bv, c:cv}))

pred_pogr = a_delta*0.02 + b_delta*0.05 + c_delta*0.1

x_verh = x.subs({a:av+a_delta, b:bv+b_delta, c:cv+c_delta})
x_niz = x.subs({a:av-a_delta, b:bv-b_delta, c:cv-c_delta})
x_sred = x.subs({a:av, b:bv, c:cv})
abs_pogr = (x_verh-x_niz)/2

print("Верхнее значение: ", x_verh)
print("Нижнее значение: ", x_niz)
print("Значение: ",x_sred)
print("Предельная абсолютная погрешность: ", pred_pogr)
print("Абсолютная погрешность: ",abs_pogr)
print("Относительная погрешность: ",abs_pogr/x_sred)
