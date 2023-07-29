from problem.objective_function import FC
from problem.constraints import define_constraints
from scipy import optimize

constraints = define_constraints()

bounds = [[33, 180], [5, 10], [5, 20], [10, 105], [6, 6], [2, 5], [2, 168], [10, 120], [5, 5]]

result = optimize.differential_evolution(FC, bounds, constraints=constraints, maxiter=4, popsize=2, disp = True, polish=False)

print(result)