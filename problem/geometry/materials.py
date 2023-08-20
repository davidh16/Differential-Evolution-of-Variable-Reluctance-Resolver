import femm
import math

def def_materials(problem):
    # dohvaćanje materijala za definiranje svojstava statora i okoline
    femm.mi_getmaterial('M-15 Steel')
    femm.mi_getmaterial('Air')

    #  dodavanje svojstava okolini
    femm.mi_addblocklabel(problem.rs2 * math.sin(math.radians(0)),
                          problem.rs2 * math.cos(math.radians(0)) - 0.5)
    femm.mi_selectlabel(problem.rs2 * math.sin(math.radians(0)),
                        problem.rs2 * math.cos(math.radians(0)) - 0.5)
    femm.mi_setblockprop('Air', 1, 0, '<None>', 0, 0, 0)
    femm.mi_clearselected()

    # dodavanje svojstava statoru
    femm.mi_addblocklabel(0, (problem.rs1 + problem.Rv) / 2)
    femm.mi_selectlabel(0, (problem.rs1 + problem.Rv) / 2)
    femm.mi_setblockprop('M-15 Steel', 1, 0, '<None>', 0, 0, 0)
    femm.mi_clearselected()

    # postavljanje granice
    femm.mi_addboundprop('Granica', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    femm.mi_selectarcsegment(-problem.Rv, 0)
    femm.mi_selectarcsegment(problem.Rv, 0)
    femm.mi_setarcsegmentprop(1, 'Granica', 0, 0)