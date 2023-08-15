import femm
import math

"""

Često se događalo da za određeni vektor skripta ne nacrta namote kako treba, odnosno cijela geometrija ne ispadne dobro,a uzrok su bili namoti.
Ovo je zahtjevalo puno debugiranja.

Svrha ovog file-a je da se testira crtanje namota kako bi se utvrdilo optimalno pozicioniranje namota oko polova kao i same dimenzije namota.
Također korištenjem file-a sam utvrdio najbolje pozicioniranje labela za namote i označavanje namota.

Usage : u file-u windings.py u funkciji generate_windings zakomentirati sve osim test.test_windings(problem)

"""

def test_windings(problem):
    x = ((problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) + 4) - (problem.rs1 * math.cos(math.radians(problem.alS1 / 2)) + 0.5)) / 2

    # za crtanje lijevog
    femm.mi_drawrectangle(
        problem.rs1*math.sin(math.radians(problem.alS1/2)) + 4,
        problem.rs1*math.cos(math.radians(problem.alS1/2)) - problem.Sp / 6,
        problem.rs1*math.sin(math.radians(problem.alS1/2)) + 0.5,
        problem.rs1*math.cos(math.radians(problem.alS1/2)) - 4*problem.Sp/6)


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

