import numpy as np
from scipy.optimize import minimize
import math

def objective(x):
    return 2 * x[0] * math.sqrt((0.5*x[0])**2 + x[1]**2) + x[0]**2
    # return A -> 2 * x[0] * math.sqrt((0.5*x[0])**2 + x[1]**2)

def constraint1(x):
    return x[0]**2 * x[1] * 0.33333 - 1500

# initial guesses
n = 2
x0 = np.zeros(n)
x0[0] = 1.0
x0[1] = 5.0

# show initial objective
print('Initial SSE Objective: ' + str(objective(x0)))

# optimize

bnds = ((0,30), (0,30))
con1 = {'type': 'ineq', 'fun': constraint1}

#con2 = {'type': 'eq', 'fun': constraint2}
cons = ([con1])
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=cons)
x = solution.x

# show final objective
print('Final SSE Objective: ' + str(objective(x)))

# print solution
print('Solution')
print('a = ' + str(x[0]))
print('h = ' + str(x[1]))
