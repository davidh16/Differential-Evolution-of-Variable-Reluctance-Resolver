import time
from problem.objective_function import FC
from scipy import optimize


if __name__=='__main__':

    bounds_object = optimize.Bounds([33, 5, 5, 2, -0.5], [180, 10, 20, 5, 4.5])

    start = time.time()

    result = optimize.differential_evolution(FC, bounds_object, maxiter=10, popsize=5, disp=True, polish=False)

    results_file = open(r"C:\Users\davidhorvat\Desktop\results.txt", "w")
    results_file.write(str(result) + "\n" + "time elapsed : " + str(time.time() - start))
    results_file.close()
