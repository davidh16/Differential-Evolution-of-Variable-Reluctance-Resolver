import femm
import numpy as np

def analyse(problem):
    femm.mi_selectcircle(0, 0, problem.rr1 + problem.DZ / 2, 4)
    femm.mi_setgroup(5)  # sva geometrija rotora

    REZ = []
    kz = 7.5  # kut zakreta rotora
    poz = int(45 / kz)

    duration = 1 / 8
    step_size = (7.5 / 360) * (1 / problem.rpm) * 60
    t = np.arange(0, duration * 60 / problem.rpm + step_size, step_size)
    time_index = 1
    exception_flag = 0

    for ji in range(poz + 1):
        exception_flag = 0

        problem.i = problem.i * np.sin(2 * np.pi * problem.f * t[time_index])

        femm.mi_setcurrent("excitation", problem.i)

        femm.mi_selectgroup(5)
        if ji > 0:
            femm.mi_moverotate(0, 0, kz)
        else:
            femm.mi_moverotate(0, 0, 0)

        femm.mi_saveas(r"C:\Users\davidhorvat\Desktop\solutions\solution" + str(ji) + ".fem")

        femm.mi_analyze(1)
        femm.mi_loadsolution()

        time_index += 1

        CIRC = femm.mo_getcircuitproperties("excitation")

        flux_linkage = CIRC[2]
        total_current = CIRC[0]

        L = np.real(flux_linkage)/np.real(total_current)

        REZ.append(np.real(L))

    AvL = sum(REZ) / len(REZ)

    return 1 / AvL

