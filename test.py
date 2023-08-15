from problem.problem_base import Problem
import femm

"""

Ovaj file je namjenjen za testiranje. 
Kada bi main funckija izbacila error za određeni vektor, 
taj isti vektor bih ubacio ovdje i pokrenio file "test.py". 
Na taj način funkcija samo nacrta geometriju, a ne radi analizu te se onda može vidjeti što je pošlo po krivu tijekom crtanja geometrije.
Korištenjem ovog file-a sam debugirao sve probleme na koje sam naišao.


vektor sa parametrima senzora
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

x = [100, 10, 15, 17, 2, 3, 5, 60, 3]

"""

bounds : [(33, 180), (5, 10), (5, 20), (10, 105), (-0.5, 3.5), (2, 5), (2, 168), (10, 120), (-0.5, 3.5)]

"""

def FCTEST(X):
    # starting the femm with predetermined configuration
    problem = Problem(x)

    # stator generation
    problem.generate_stator()

    # rotor generation
    problem.generate_rotor()

    # windings generation
    problem.generate_windings()

    femm.mi_saveas(r"C:\Users\davidhorvat\Desktop\test.fem")

FCTEST(x)