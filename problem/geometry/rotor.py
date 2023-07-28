import femm
import math


def generate_rotor(problem):

    # kut zaobljenja za crtanje lukova za glavu pola
    if problem.Pr != 3:
        arc_angle = (360 / problem.Pr) / 2
    else:
        """
        U slučaju kada je broj polova 3, a arc_angle se postavi : arc_angle = (360 / problem.Pr) / 2, 
        glava pola rotora dobije nepravilan oblik. Nastane udubljenje u sredini, stoga je potrebno malo povećati kut zaobljenja.
        """
        arc_angle = (360 / problem.Pr) / 2.5

    # crtanje glave pola s obzirom na broj polova (u slučaju kada su 2 pola, crtanje ima drugačiji algoritam)
    if problem.Pr == 2:

        # crtanje čvorova glave pola rotora
        femm.mi_addnode(0, problem.rr2)
        femm.mi_selectnode(0, problem.rr2)
        femm.mi_copyrotate(0, 0, problem.alR1/2, 1)
        femm.mi_selectnode(0, problem.rr2)
        femm.mi_moverotate(0, 0, -problem.alR1/2)

        # spajanje nacrtanih čvorova
        femm.mi_addarc(problem.rr2 * math.cos(math.radians(90 - problem.alR1/2)),
                       problem.rr2 * math.sin(math.radians(90 - problem.alR1/2)),
                       problem.rr2 * math.cos(math.radians(90 + problem.alR1/2)),
                       problem.rr2 * math.sin(math.radians(90 + problem.alR1/2)),
                       arc_angle, 1)

        # selektiranje i stvaranje druge kopije glave pola
        femm.mi_selectarcsegment(0, problem.rr2)
        femm.mi_copyrotate(0, 0, 360 / problem.Pr, 1)

        # spajanje dva pola jednim lukom
        femm.mi_addarc(problem.rr2 * math.cos(math.radians(90 + problem.alR1/2)),
                       problem.rr2 * math.sin(math.radians(90 + problem.alR1/2)),
                       problem.rr2 * math.cos(math.radians(270 - problem.alR1/2)),
                       problem.rr2 * math.sin(math.radians(270 - problem.alR1/2)),
                       arc_angle, 1)

        #selektiranje luka koji spaja polove i stvaranje kopije na drugoj strani (zrcaljenje)
        femm.mi_selectarcsegment(-1, 0)
        femm.mi_mirror(0,1,0,-1)

        # dodavanje svojstava rotoru
        femm.mi_addblocklabel((problem.rV + problem.rr2) / 2, 0)
        femm.mi_selectlabel((problem.rV + problem.rr2) / 2, 0)
        femm.mi_setblockprop('M-15 Steel', 1, 0, '<None>', 0, 0, 0)
        femm.mi_clearselected()

        # crtanje osovine
        femm.mi_addnode(0, problem.rV)
        femm.mi_addnode(0, -problem.rV)
        femm.mi_addarc(0, problem.rV, 0, -problem.rV, 180, 1)
        femm.mi_addarc(0, -problem.rV, 0, problem.rV, 180, 1)

        # dodavanje svojstava osovini
        femm.mi_addblocklabel(problem.rV / 2, problem.rV / 2)
        femm.mi_selectlabel(problem.rV / 2, problem.rV / 2)
        femm.mi_setblockprop('Copper', 1, 0, '<None>', 0, 0, 0)
        femm.mi_clearselected()

    else:

        # crtanje čvorova glave pola rotora
        femm.mi_addnode(0, problem.rr1)
        femm.mi_addnode(0, problem.rr2)
        femm.mi_selectnode(0, problem.rr2)
        femm.mi_copyrotate(0, 0, problem.alR1/2, 1)
        femm.mi_selectnode(0, problem.rr2)
        femm.mi_moverotate(0, 0, -problem.alR1/2)

        # crtanje lijeve polovice glave pola rotora
        femm.mi_addarc(0,
                       problem.rr1,
                       problem.rr2 * math.cos(math.radians(90 + problem.alR1/2)),
                       problem.rr2 * math.sin(math.radians(90 + problem.alR1/2)),
                       arc_angle, 1)

        # crtanje desne polovice glave pola rotora
        femm.mi_addarc(problem.rr2 * math.cos(math.radians(90 - problem.alR1/2)),
                       problem.rr2 * math.sin(math.radians(90 - problem.alR1/2)),
                       0,
                       problem.rr1,
                       arc_angle, 1)

        # selektiranje obje polovice glave pola rotora, grupiranje i stvaranje jedne kopije
        femm.mi_selectarcsegment(-1,problem.rr2, )
        femm.mi_selectarcsegment(1,problem.rr2, )
        femm.mi_setgroup(4)
        femm.mi_selectgroup(4)
        femm.mi_copyrotate(0, 0, 360 / problem.Pr, 1)

        # spajanje dva susjedna pola rotora
        femm.mi_addarc(
            problem.rr2 * math.cos(math.radians(360/problem.Pr + 90 - problem.alR1/2)),
            problem.rr2 * math.sin(math.radians(360/problem.Pr + 90 - problem.alR1/2)),
            problem.rr2 * math.cos(math.radians(90 + problem.alR1/2)),
            problem.rr2 * math.sin(math.radians(90 + problem.alR1/2)),
            arc_angle/2, 1)

        # selektiranje spojenih polova rotora, grupiranje i stvaranje preostalih kopija
        femm.mi_selectcircle(0, 0, problem.rr1, 4)
        femm.mi_setgroup(5)
        femm.mi_selectgroup(5)
        femm.mi_copyrotate(0, 0, 360 / problem.Pr, problem.Pr - 1)

        # dodavanje svojstava rotoru
        femm.mi_addblocklabel((problem.rV + problem.rr2) / 2, 0)
        femm.mi_selectlabel((problem.rV + problem.rr2) / 2, 0)
        femm.mi_setblockprop('M-15 Steel', 1, 0, '<None>', 0, 0, 0)
        femm.mi_clearselected()

        # crtanje osovine
        femm.mi_addnode(0, problem.rV)
        femm.mi_addnode(0, -problem.rV)
        femm.mi_addarc(0, problem.rV, 0, -problem.rV, 180, 1)
        femm.mi_addarc(0, -problem.rV, 0, problem.rV, 180, 1)

        # dodavanje svojstava osovini
        femm.mi_addblocklabel(problem.rV / 2, problem.rV / 2)
        femm.mi_selectlabel(problem.rV / 2, problem.rV / 2)
        femm.mi_setblockprop('Copper', 1, 0, '<None>', 0, 0, 0)
        femm.mi_clearselected()


