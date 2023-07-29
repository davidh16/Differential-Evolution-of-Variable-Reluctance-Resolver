import math
from scipy import optimize
import numpy as np

def define_constraints():

    stator_poles_inequality_constraint = lambda x: x[3] - (360 / x[4])

    rotor_pole_angle_constraint = lambda x: x[8] - (360 / x[7])

    math_constraint_rotor = lambda x: (math.sin(math.radians(x[7] / 2)) * (x[0] - x[1] - x[2] - x[5])) / (
                x[0] - x[1] - x[2] - x[5] - x[6])

    math_constraint_stator = lambda x: (math.sin(math.radians(x[3] / 2)) * (x[0] - x[1]) / (x[0] - x[1] - x[2]))

    # stator pole angle constraint
    constraint1 = optimize.NonlinearConstraint(stator_poles_inequality_constraint, -np.inf, -15)

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