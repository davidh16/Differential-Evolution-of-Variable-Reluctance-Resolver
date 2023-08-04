from problem.objective_function import FC
from problem.problem_base import Problem
import femm

"""

Ovaj file je namjenjen za testiranje. 
Kada bi main funckija izbacila error za određeni vektor, 
taj isti vektor bih ubacio ovdje i zakomentirao bih dio u objective_function koji se odnosi na analizu. 
Na taj način funkcija samo nacrta geometriju, a ne radi analizu te se onda može vidjeti što je pošlo po krivu tijekom crtanja geometrije.
Korištenjem ovog file-a sam debugirao sve probleme na koje sam naišao.
U komentarima su zapisani primjeri vektora koji su stvarali probleme, no ti isti problemi su riješeni.

Usage : odrediti vektor x, otkomentirati liniju 30, pokrenuti test.py

"""
x = [99.9631171, 7.07432642, 5.42466828, 31.35358989, 0.14694722, 2.11299388, 3.43070733, 119.47654249, -0.49148282]

"""

[146.21466081, 7.39159116, 16.07664157, 12.82642157, 2.87297219, 2.29427683, 2.32183008, 34.15334476, 0.48284293]

[87.09315335, 7.79408624, 14.82106205, 58.0580431, 1.07910747, 4.16963895, 5.52506552, 50.23474978, 1.62226178] - constraint

"""

def FCTEST(X):
    # starting the femm with predetermined configuration
    problem = Problem(x)

    # generiranje statora
    problem.generate_stator()

    # generiranje rotora
    problem.generate_rotor()

    # generiranje namota
    problem.generate_windings()

    femm.mi_saveas(r"C:\Users\davidhorvat\Desktop\test.fem")

FCTEST(x)