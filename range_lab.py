import sympy 
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

x = symbols('x')
f = 2*x + 1
plot(f)