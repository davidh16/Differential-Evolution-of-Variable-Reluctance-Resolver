import math
from scipy import optimize
import numpy as np


def define_constraints():
    broj_polova_statora = [3, 6, 9, 12]
    broj_polova_rotora = [2, 3, 4, 5]

    # o = lambda x: 2*math.pi*(x[0]-x[1]-x[2])
    # max_arc_length = lambda x: 0 / broj_polova_statora[round((x[4]))]
    # max_alpha = lambda x:max_arc_length /(x[0]-x[1]-x[2]) - 30


    stator_poles_inequality_constraint = lambda x: x[3] - (2*math.pi*(x[0]-x[1]-x[2]) / broj_polova_statora[round((x[4]))])/(x[0]-x[1]-x[2]) - 30

    rotor_pole_angle_constraint = lambda x: x[7] - (360 / broj_polova_rotora[round(x[8])])

    math_constraint_rotor = lambda x: (math.sin(math.radians(x[7] / 2)) * (x[0] - x[1] - x[2] - x[5])) / (
                x[0] - x[1] - x[2] - x[5] - x[6])

    math_constraint_stator = lambda x: (math.sin(math.radians(x[3] / 2)) * (x[0] - x[1]) / (x[0] - x[1] - x[2]))

    # stator pole angle constraint
    constraint1 = optimize.NonlinearConstraint(stator_poles_inequality_constraint, -np.inf, 0)

    # rotor pole length constraint
    constraint2 = optimize.LinearConstraint([-1, 1, 1, 0, 0, 1, 1, 0, 0], -np.inf, 0)

    # rotor pole angle constraint
    constraint3 = optimize.NonlinearConstraint(rotor_pole_angle_constraint, -np.inf, 0)

    # math constraint rotor
    constraint4 = optimize.NonlinearConstraint(math_constraint_rotor, -1, 1)

    # math constraint stator
    constraint5 = optimize.NonlinearConstraint(math_constraint_stator, -1, 1)

    constraints = (constraint1, constraint2, constraint3, constraint4, constraint5)

    return constraints
