import femm
import math


def generate_stator(problem):
    # crtanje vanjskog ruba statora
    femm.mi_addnode(0, problem.Rv)
    femm.mi_addnode(0, -problem.Rv)
    femm.mi_addarc(0, problem.Rv, 0, -problem.Rv, 180, 1)
    femm.mi_addarc(0, -problem.Rv, 0, problem.Rv, 180, 1)

    ##### Pol statora #####

    # crtanje čvorova donjeg brida pola
    femm.mi_addnode(0, problem.rs1)
    femm.mi_selectnode(0, problem.rs1)
    femm.mi_copyrotate(0, 0, problem.alS1 / 2, 1)
    femm.mi_selectnode(0, problem.rs1)
    femm.mi_moverotate(0, 0, -problem.alS1 / 2)

    femm.mi_selectrectangle(-math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1) - 0.5,
                   math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1) + 0.5,
                   -math.sin(math.radians(-problem.alS1 / 2)) * (problem.rs1)+0.5,
                   math.cos(math.radians(-problem.alS1 / 2)) * (problem.rs1)-0.5)

    femm.mi_setgroup(99)
    femm.mi_selectgroup(99)
    femm.mi_copytranslate(0, -problem.Sp, 1)

    # crtanje gornjeg brid pola
    femm.mi_addarc(-math.sin(math.radians(-problem.alS1 / 2)) * (problem.rs1),
                   math.cos(math.radians(-problem.alS1 / 2)) * (problem.rs1) - problem.Sp,
                   -math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                   math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1) - problem.Sp,
                   360/problem.Ps, 1)

    # crtanje lijevog brida pola
    femm.mi_addsegment(math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1) - problem.Sp)

    # crtanje desnog brida pola
    femm.mi_addsegment(-math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       -math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                       math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1) - problem.Sp)

    # označavanje svih kreiranih djelova
    femm.mi_selectrectangle(-math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1) - 0.5,
                            math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1) + 0.5,
                            -math.sin(math.radians(-problem.alS1 / 2)) * (problem.rs1) + 0.5,
                            math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1) - problem.Sp - 0.5)

    # grupiranje označenih djelova i kopiranje s obzirom na broj polova
    femm.mi_setgroup(1)
    femm.mi_selectgroup(1)
    femm.mi_copyrotate(0, 0, 360 / problem.Ps, problem.Ps - 1)

    # spajanje polova kako bi se kreirao unutarnji rub statora
    femm.mi_addarc(-math.sin(math.radians(problem.alS1 / 2)) * problem.rs1,
                   math.cos(math.radians(problem.alS1 / 2)) * problem.rs1,
                   -math.sin(math.radians(problem.alS1 / 2 + problem.kutS)) * problem.rs1,
                   math.cos(math.radians(problem.alS1 / 2 + problem.kutS)) * problem.rs1, problem.kutS, 1)

    femm.mi_selectarcsegment(-math.sin(math.radians(problem.alS1 / 2)) * (problem.rs1),
                             math.cos(math.radians(problem.alS1 / 2)) * (problem.rs1))
    femm.mi_copyrotate(0, 0, 360 / problem.Ps, problem.Ps - 1)

    femm.mi_selectcircle(0,0, problem.Rv, 4)
    femm.mi_setgroup(25)
    femm.mi_clearselected()
