import femm
import math

def generate_excitation_windings(problem):

    x = ((problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) + 3) - (problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) + 0.3)) / 2

    # crtanje prvokutnika s desne strane pola
    femm.mi_drawrectangle(
        problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 3,
        problem.rs1 * math.cos(math.radians(-problem.alS1 / 2)) - problem.Sp / 5,
        problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 0.3,
        problem.rs1 * math.cos(math.radians(-problem.alS1 / 2)) - 7 * problem.Sp / 10)

    # dodavanje materijala i strujnog kruga pravokutniku
    femm.mi_addblocklabel(problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 3 + x,
                          problem.rs1 * math.cos(math.radians(-problem.alS1 / 2)) - 9 * problem.Sp / 20)
    femm.mi_selectlabel(problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 3 + x,
                        problem.rs1 * math.cos(math.radians(-problem.alS1 / 2)) - 9 * problem.Sp / 20)
    femm.mi_setblockprop('Copper', 1, 0, 'excitation', 0, 0, 50)

    femm.mi_clearselected()

    # # # crtanje prvokutnika s lijeve strane pola
    femm.mi_drawrectangle(
        problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 3,
        problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) - problem.Sp / 5,
        problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 0.3,
        problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) - 7 * problem.Sp / 10)

    # dodavanje materijala i strujnog kruga pravokutniku
    femm.mi_addblocklabel(problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 3 - x,
                          problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) - 9 * problem.Sp / 20)
    femm.mi_selectlabel(problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 3 - x,
                        problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) - 9 * problem.Sp / 20)
    femm.mi_setblockprop('Copper', 1, 0, 'excitation', 0, 0, -50)

    femm.mi_clearselected()

    # selektiranje oba pravokutnika, grupiranje i kopiranje s obzirom na broj polova
    femm.mi_selectrectangle(
        problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 3.1,
        problem.rs1 * math.cos(math.radians(-problem.alS1 / 2)) - problem.Sp / 5 + 0.1,
        problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 0.2,
        problem.rs1 * math.cos(math.radians(-problem.alS1 / 2)) - 7 * problem.Sp / 10 - 0.1)

    femm.mi_selectrectangle(
        problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 3.1,
        problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) - problem.Sp / 6 + 0.1,
        problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 0.2,
        problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) - 7 * problem.Sp / 10 - 0.1)

    femm.mi_setgroup(15)


    if problem.Ps/3 != 1:

        femm.mi_selectgroup(15)
        femm.mi_copyrotate(0, 0, 360/(problem.Ps/3), problem.Ps/3 -1)
        femm.mi_clearselected()






