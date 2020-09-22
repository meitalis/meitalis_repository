import numpy as np
from scipy.optimize import minimize
import math

# def objective(x):
#     return 2 * x[0] - 3 * x[1]
#
# def objective_w(x):
#     return 0.5 * (2 * x[0] - 3 * x[1]) + 0.5 * (2*x[0] + x[1])
#
# def constraint1(x):
#     return (-1) * 7 + x[0] + 5 * x[1]
#
# def constraint2(x):
#     return -10 + 4 * x[0] + x[1]
#
# def constraint3(x):
#     return 7 * x[0] - 6 * x[1] + 9
#
# def constraint4(x):
#     return x[0] - 6 * x[1] + 24
###########################################
def objective_w1(x):
    return 0.5 * x[0] + 0.5 * x[1]

def constraint5(x):
    return (x[0] ** 2) + (x[1] ** 2) - 1
###########################################
# initial guesses
n = 2
x0 = np.zeros(n)
x0[0] = 1.0
x0[1] = 1.0

# show initial objective
print('Initial SSE Objective: ' + str(round(objective_w1(x0))))

# optimize

bnds = ((0,5), (0,5))
# con1 = {'type': 'ineq', 'fun': constraint1}
# con2 = {'type': 'ineq', 'fun': constraint2}
# con3 = {'type': 'ineq', 'fun': constraint3}
# con4 = {'type': 'ineq', 'fun': constraint4}
con5 = {'type': 'eq', 'fun': constraint5}

#con2 = {'type': 'eq', 'fun': constraint2}
#cons = ([con1,con2,con3,con4])
cons = ([con5])
solution = minimize(objective_w1,x0,method='SLSQP',\
                    bounds=bnds,constraints=cons)
x = solution.x

# show final objective
print('Final SSE Objective: ' + str(round(objective_w1(x))))

# print solution
print('Solution')
print('X1 = ' + str(round(x[0],3)))
print('X2 = ' + str(round(x[1],3)))
#################################################################






