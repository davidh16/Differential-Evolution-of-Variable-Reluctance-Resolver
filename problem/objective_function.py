import femm
from problem.problem_base import Problem
import numpy as np

""""
vektor sa parametrima senzora :

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

def FC(x):

    # starting the femm with predetermined configuration
    problem = Problem(x)

    # stator generation
    problem.generate_stator()

    # rotor generation
    problem.generate_rotor()

    # windings generation
    problem.generate_windings()

    # grouping of the whole rotor geometry
    femm.mi_selectcircle(0, 0, problem.rr1 + problem.DZ / 2, 4)
    femm.mi_setgroup(5)

    # matrix to store results in
    REZ = []

    # angle of rotation for each step
    kz = 7.5
    poz = int(45 / kz)

    # making of time vector
    duration = 1 / 8
    step_size = (7.5 / 360) * (1 / problem.rpm) * 60
    t = np.arange(0, duration * 60 / problem.rpm + step_size, step_size)
    time_index = 1

    for ji in range(poz + 1):

        problem.i = problem.i * np.sin(2 * np.pi * 5000 * t[time_index])

        femm.mi_setcurrent("excitation", problem.i)

        femm.mi_selectgroup(5)
        if ji > 0:
            femm.mi_moverotate(0, 0, kz)
        else:
            femm.mi_moverotate(0, 0, 0)

        femm.mi_saveas(r"C:\Users\davidhorvat\Desktop\solutions\solution" + str(ji) + ".fem")

        try:
            femm.mi_analyze(1)
        except Exception:
            print("# analyze error occurred")
            # print(x)
            return 100000

        try:
            femm.mi_loadsolution()
        except Exception:
            print("# loading solution error occurred")
            # print(x)
            return 100000

        time_index += 1

        circ = femm.mo_getcircuitproperties("excitation")

        flux_linkage = circ[2]
        total_current = circ[0]

        if total_current != 0:
            l = flux_linkage / total_current
            REZ.append(l)
        else:
            REZ.append(0)

    avg_l = sum(REZ) / len(REZ)
    result = 1 / avg_l

    return result



