import numpy as np
from scipy.optimize import minimize


def objective(x):
    return x[2] # lamda

def constraint1(x):
    return (-0.5 * x[0]) - (0.5 * x[1]) - 1 + x[2]

def constraint2(x):
    return x[0] ** 2 + x[1] ** 2 - 1

###########################################
# initial guesses
n = 3
x0 = np.zeros(n)
x0[0] = 0.5
x0[1] = 0
x0[2] = 1.0

# show initial objective
print('Initial SSE Objective: ' + str(round(objective(x0))))

# optimize

bnds = ((-5,5), (-5,5),(-5,5))
# con1 = {'type': 'ineq', 'fun': constraint1}
# con2 = {'type': 'ineq', 'fun': constraint2}
# con3 = {'type': 'ineq', 'fun': constraint3}
con4 = {'type': 'ineq', 'fun': constraint1}
con5 = {'type': 'eq', 'fun': constraint2}

#con2 = {'type': 'eq', 'fun': constraint2}
#cons = ([con1,con2,con3,con4])
cons = ([con4,con5])
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=cons)
x = solution.x

# show final objective
print('Final SSE Objective: ' + str(round(objective(x))))

# print solution
print('Solution')
print('X1 = ' + str(x[0]))
print('X2 = ' + str(x[1]))
print('X3 = ' + str(x[2]))
#################################################################






