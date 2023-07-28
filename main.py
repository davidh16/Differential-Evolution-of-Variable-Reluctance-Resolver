from problem.objective_function import FC
import math
import numpy as np
from scipy import optimize

# primjer geometrije za koju dobije math domain error
# x = [20, 5, 5, 15, 12, 3, 5, 60, 3]

# primjer geometrije za koju iz nekog razloga ne crta sve namote
# x= [57.50671650703761, 6.821416974078076, 5, 12.097145205282159, 6, 2.1109872261963227, 24.229191393943324, 33.73677550393755, 5]


""""
vektor sa parametrima senzora
x = [
      vanjski_promjer_statora,
      debljina_jarma_statora, 
      duljina_pola_statora, 
      kut_pola_statora, 
      broj_polova_statora,
      duljina_zracnog_raspora,
      duljina_pola_rotora,
      kut_pola_rotora,
      broj_polova_rotora
     ]

     primjer : x = [100, 20, 5, 30, 6, 3, 5, 60, 3]
"""


stator_poles_inequality_constraint = lambda x: x[3] - (360 / x[4])

rotor_pole_angle_constraint = lambda x: x[8] - (360 / x[7])

math_constraint_rotor = lambda x: (math.sin(math.radians(x[7] / 2)) * (x[0] - x[1] - x[2] - x[5])) / (x[0] - x[1] - x[2] - x[5] - x[6])

math_constraint_stator = lambda x: (math.sin(math.radians(x[3] / 2)) * (x[0]-x[1]) / (x[0]-x[1]-x[2]))

def equality_constraint(x):
    return x[4] - 3

# stator poles constraint
#constraint1 = optimize.LinearConstraint([0, 0, 0, 0, 1, 0, 0, 0, 0], 6, 6)
# lb1 = [0,0,0,0,6,0,0,0,0]
# ub1 = [0,0,0,0,6,0,0,0,0]
# constraint1 = optimize.Bounds([lb1[4]],[ub1[4]])

# rotor poles constraint
#constraint7 = optimize.LinearConstraint([0, 0, 0, 0, 0, 0, 0, 0, 1], 5, 5)
# lb7 = [0,0,0,0,0,0,0,0,5]
# ub7 = [0,0,0,0,0,0,0,0,5]
# constraint7 = optimize.Bounds([lb1[8]],[ub1[8]])

# stator pole angle constraint
constraint2 = optimize.NonlinearConstraint(stator_poles_inequality_constraint, -np.inf, -15)

# rotor pole length constraint
constraint3 = optimize.LinearConstraint([-1, 1, 1, 0, 0, 1, 1, 0, 0], -np.inf, 0)

# rotor pole angle constraint
constraint4 = optimize.NonlinearConstraint(rotor_pole_angle_constraint, -np.inf, 0)

# math constraint rotor
constraint5 = optimize.NonlinearConstraint(math_constraint_rotor, -1, 1)

# math constraint stator
constraint6 = optimize.NonlinearConstraint(math_constraint_stator, -1, 1)

constraints = (constraint5, constraint2, constraint3, constraint4, constraint6)

# bounds = [(33,180),(5,10),(5,20),(10,105),(3,12),(2,5),(2,168),(10,120),(2,6)]
bounds = [[33, 180], [5, 10], [5, 20], [10, 105], [6, 6], [2, 5], [2, 168], [10, 120], [5, 5]]

result = optimize.differential_evolution(FC, bounds, constraints=constraints)

print(result)