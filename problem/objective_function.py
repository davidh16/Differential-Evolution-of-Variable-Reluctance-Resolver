import femm
from problem.problem_base import Problem

""""
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

#generating geometry vector
# x = geometry_base.generate_geometry_vector()

# x = [100, 20, 11.5, 30, 6, 3, 5, 60, 3]

def FC(x):

    print(x)

    # starting the femm with predetermined configuration
    problem = Problem(x)

    # generiranje statora
    problem.generate_stator()

    # generiranje rotora
    problem.generate_rotor()

    # generiranje namota
    problem.generate_windings()

    femm.mi_saveas(r"C:\Users\davidhorvat\Desktop\test.fem")

    print(problem.analyse())

    # print("rezultat :", result)
    #
    # return result



