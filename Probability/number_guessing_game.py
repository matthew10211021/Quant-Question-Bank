import scipy.integrate as integrate
from scipy.optimize import minimize

upper = 924

def cost(x, y):
    if y < x: return (x-y)**2
    else: return (y-x)*2

def f(x):
    return integrate.quad(lambda y: cost(x, y), 0, upper)[0]

print(minimize(f, 1).x[0])