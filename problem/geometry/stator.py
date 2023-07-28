import femm
import math


def generate_stator(problem):
    # crtanje vanjskog ruba statora
    femm.mi_addnode(0, problem.Rv)
    femm.mi_addnode(0, -problem.Rv)
    femm.mi_addarc(0, problem.Rv, 0, -problem.Rv, 180, 1)
    femm.mi_addarc(0, -problem.Rv, 0, problem.Rv, 180, 1)

    # dohvaćanje materijala za definiranje svojstava statora i okoline
    femm.mi_getmaterial('M-15 Steel')
    femm.mi_getmaterial('Air')

    #  dodavanje svojstava okolini
    femm.mi_addblocklabel(math.sin(math.radians(problem.alS2 / 2 + problem.kutS / 2)) * (problem.rs1 + problem.rs2) / 2,
                          math.cos(math.radians(problem.alS2 / 2 + problem.kutS / 2)) * (problem.rs1 + problem.rs2) / 2)
    femm.mi_selectlabel(math.sin(math.radians(problem.alS2 / 2) + problem.kutS / 2) * (problem.rs1 + problem.rs2) / 2,
                        math.cos(math.radians(problem.alS2 / 2) + problem.kutS / 2) * (problem.rs1 + problem.rs2) / 2)
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

    ##### Pol statora #####

    # crtanje čvorova donjeg brida pola
    femm.mi_addnode(0, problem.rs1)
    femm.mi_selectnode(0, problem.rs1)
    femm.mi_copyrotate(0, 0, problem.alS1 / 2, 1)
    femm.mi_selectnode(0, problem.rs1)
    femm.mi_moverotate(0, 0, -problem.alS1 / 2)

    # crtanje čvorova gornjeg brida pola
    femm.mi_addnode(0, problem.rs2)
    femm.mi_selectnode(0, problem.rs2)
    femm.mi_copyrotate(0, 0, problem.alS2 / 2, 1)
    femm.mi_selectnode(0, problem.rs2)
    femm.mi_moverotate(0, 0, -problem.alS2 / 2)

    # crtanje gornjeg brid pola
    femm.mi_addarc(math.sin(math.radians(problem.alS2 / 2)) * (problem.rs2),
                   math.cos(math.radians(problem.alS2 / 2)) * (problem.rs2),
                   -math.sin(math.radians(problem.alS2 / 2)) * (problem.rs2),
                   math.cos(math.radians(problem.alS2 / 2)) * (problem.rs2), problem.alS2, 1)

    # crtanje lijevog brida pola
    femm.mi_addsegment(math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       math.sin(math.radians(problem.alS2 / 2)) * (problem.rs2),
                       math.cos(math.radians(problem.alS2 / 2)) * (problem.rs2))

    # crtanje desnog brida pola
    femm.mi_addsegment(-math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       -math.sin(math.radians(problem.alS2 / 2)) * (problem.rs2),
                       math.cos(math.radians(problem.alS2 / 2)) * (problem.rs2))

    # označavanje svih kreiranih djelova
    femm.mi_selectarcsegment(math.sin(math.radians(problem.alS2 / 2)) * (problem.rs2),
                             math.cos(math.radians(problem.alS2 / 2)) * (problem.rs2))
    femm.mi_selectarcsegment(-math.sin(math.radians(problem.alS2 / 2)) * (problem.rs2),
                             math.cos(math.radians(problem.alS2 / 2)) * (problem.rs2))
    femm.mi_selectarcsegment(0, problem.rs2)
    femm.mi_selectsegment(-math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                          math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1))
    femm.mi_selectsegment(math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                          math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1))

    # grupiranje označenih djelova i kopiranje s obzirom na broj polova
    femm.mi_setgroup(1)
    femm.mi_selectgroup(1)
    femm.mi_copyrotate(0, 0, 360 / problem.Ps, problem.Ps - 1)

    # spajanje polova kako bi se kreirao unutarnji rub statora
    femm.mi_addarc(-math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                   math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1),
                   -math.sin(math.radians(problem.kutS + problem.alS1 / 2)) * (problem.rs1),
                   math.cos(math.radians(problem.kutS + problem.alS1 / 2)) * (problem.rs1), problem.kutS, 1)

    femm.mi_selectarcsegment(-math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                             math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1))
    femm.mi_copyrotate(0, 0, 360 / problem.Ps, problem.Ps - 1)

    femm.mi_selectcircle(0,0, problem.Rv, 4)
    femm.mi_setgroup(25)
    femm.mi_clearselected()
