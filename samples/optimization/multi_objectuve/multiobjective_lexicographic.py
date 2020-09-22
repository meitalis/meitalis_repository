import numpy as np
from scipy.optimize import minimize
import math

def objective(x):
    return 4 * x[0] + x[1]

def constraint1(x):
    return (-1) * 7 + x[0] + 5 * x[1]

def constraint2(x):
    return -10 + 4 * x[0] + x[1]

def constraint3(x):
    return 7 * x[0] - 6 * x[1] + 9

def constraint4(x):
    return x[0] - 6 * x[1] + 24

# initial guesses
n = 2
x0 = np.zeros(n)
x0[0] = 3
x0[1] = 4

# show initial objective
print('Initial SSE Objective: ' + str(round(objective(x0),4)))

# optimize

bnds = ((0.5,3), (0.5,4))
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3}
con4 = {'type': 'ineq', 'fun': constraint4}

cons = ([con1,con2,con3,con4])

# solution = minimize(objective,x0,method='SLSQP',\
#                     bounds=bnds,constraints=cons)
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds)

ss = solution.x
print(type(ss))
print(ss)

# show final objective
print('Final SSE Objective: ' + str(round(objective(ss),5)))

# print solution
print('Solution')
print('X1 = ' + str(round(ss[0],5)))
print('X2 = ' + str(round(ss[1],5)))
#################################################################






