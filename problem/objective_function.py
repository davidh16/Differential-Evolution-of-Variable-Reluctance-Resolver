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

    # generiranje statora
    problem.generate_stator()

    # generiranje rotora
    problem.generate_rotor()

    # generiranje namota
    problem.generate_windings()

    femm.mi_saveas(r"C:\Users\davidhorvat\Desktop\test.fem")

    femm.mi_selectcircle(0, 0, problem.rr1 + problem.DZ / 2, 4)
    femm.mi_setgroup(5)  # sva geometrija rotora

    REZ = []
    kz = 7.5  # kut zakreta rotora
    poz = int(45 / kz)

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

        # za neke vektore koji se rijetko generiraju ne valja geometrija i nastane error, u slučaju kada dođe do errora, funckija vraća penalty value 100000
        try:
            femm.mi_analyze(1)
        except Exception:
            print("error occuerd")
            print(x)
            return 100000

        # femm.mi_analyze(1)
        femm.mi_loadsolution()

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



