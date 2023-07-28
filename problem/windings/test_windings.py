import femm
import math

def test_windings(problem):
    x = ((problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) + 4) - (problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) + 0.5)) / 2

    # za crtanje lijevog
    femm.mi_drawrectangle(
        problem.rs1*math.sin(math.radians(problem.alS1/2)) + 4,
        problem.rs1*math.cos(math.radians(problem.alS1/2)) - problem.Sp / 6,
        problem.rs1*math.sin(math.radians(problem.alS1/2)) + 0.5,
        problem.rs1*math.cos(math.radians(problem.alS1/2)) - 4*problem.Sp/6)


    print("ovo je rs1", problem.rs1)

    # za crtanje desnog
    femm.mi_drawrectangle(
        problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 4,
        problem.rs1 * math.cos(math.radians(-problem.alS1/2)) - problem.Sp / 6,
        problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 0.5,
        problem.rs1 * math.cos(math.radians(-problem.alS1/2)) - 4*problem.Sp/6)

    # za označavanje lijevog
    femm.mi_selectrectangle(
        problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 4.1,
        problem.rs1 * math.cos(math.radians(problem.alS1/2)) - problem.Sp / 6 + 0.1,
        problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 0.4,
        problem.rs1 * math.cos(math.radians(problem.alS1/2)) - 4*problem.Sp/6 - 0.1)


    # za označavanje desnog
    femm.mi_selectrectangle(
        problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 4.1,
        problem.rs1 * math.cos(math.radians(-problem.alS1/2)) - problem.Sp / 6 + 0.1,
        problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 0.4,
        problem.rs1 * math.cos(math.radians(-problem.alS1/2)) - 4*problem.Sp/6 - 0.1)

    # za label desnog
    femm.mi_addnode(problem.rs1 * math.sin(math.radians(-problem.alS1 / 2)) - 4 + x,
                    problem.rs1 * math.cos(math.radians(-problem.alS1/2)) - 5*problem.Sp/12)

    # za label lijevog
    femm.mi_addnode(problem.rs1 * math.sin(math.radians(problem.alS1 / 2)) + 4 - x,
                    problem.rs1 * math.cos(math.radians(problem.alS1/2)) - 5*problem.Sp/12)

