import numpy as np
import sympy as sp
from sympy.integrals import inverse_laplace_transform

s = sp.symbols('s')
t = sp.symbols('t', positive = True)
tf = (20) / 103 * (s + 3) 

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t
from sympy import pprint
a = Symbol('a', positive=True)
x1 = inverse_laplace_transform(tf, s, t)

#############

s = sp.symbols('s')
t = sp.symbols('t', positive = True)
tf = (-7) / 54 * (s + 4) 

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t
from sympy import pprint
a = Symbol('a', positive=True)
x2 = inverse_laplace_transform(tf, s, t)

###############

s = sp.symbols('s')
t = sp.symbols('t', positive = True)
tf = (5203 * s + 5200) / 5562 * (s ** 2 + 2 * s + 100) 

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t
from sympy import pprint
a = Symbol('a', positive=True)
x3 = inverse_laplace_transform(tf, s, t)

#############

pprint(x1 + x2 + x3)  

