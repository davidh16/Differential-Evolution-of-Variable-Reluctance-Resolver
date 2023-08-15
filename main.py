import time
from problem.objective_function import FC
from problem.constraints import define_constraints
from scipy import optimize


if __name__=='__main__':

    constraints = define_constraints()

    bounds_object = optimize.Bounds([33, 5, 5, 10, -0.5, 2, 2, 10, -0.5], [180, 10, 20, 105, 3.5, 5, 168, 120, 3.5])

    start = time.time()

    result = optimize.differential_evolution(FC, bounds_object, constraints=constraints, maxiter=100, popsize=10, disp=True)

    results_file = open(r"C:\Users\davidhorvat\Desktop\results.txt", "w")
    results_file.write(str(result) + "\n" + "time elapsed : " + str(time.time() - start))
    results_file.close()
