import numpy as np         
import sympy as sp
from sympy.integrals import inverse_laplace_transform

s = sp.symbols('s')
t = sp.symbols('t', positive = True)
tf = (-266) / (93 * (s + 8))                 

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t
from sympy import pprint
a = Symbol('a', positive=True)
x1 = inverse_laplace_transform(tf, s, t)   
  #
s = sp.symbols('s')
t = sp.symbols('t', positive = True)
tf = (1199 * s + 534) / (417 * (s ** 2 + 8 * s + 3))

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t
from sympy import pprint
a = Symbol('a', positive=True)
x2 = inverse_laplace_transform(tf,s,t)
#############
s = sp.symbols('s')
t = sp.symbols('t', positive = True)
tf = (-65 * s - 1014) / (4309 * (s ** 2 + 5 * s + 7))

from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t
from sympy import pprint
a = Symbol('a', positive=True)
x3 = inverse_laplace_transform(tf,s,t)

pprint(x1 + x2 + x3) 
