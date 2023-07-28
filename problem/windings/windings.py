import femm
import problem.windings.test_windings as test
import problem.windings.excitation_windings as e
import problem.windings.sin_windings as sin
import problem.windings.cos_windings as cos

"""
grupa statora = 25
grupa uzbudnih namota = 15
grupa sinusnih namota = 16
grupa kosinusnih namota = 17
"""

def generate_windings(problem):

    femm.mi_getmaterial('Copper')
    femm.mi_addcircprop("excitation", problem.i, 1)
    femm.mi_addcircprop("sin", 0, 1)
    femm.mi_addcircprop("cos", 0, 1)

    # dodjeljivanje svojstava uzbudnom namotu
    e.generate_excitation_windings(problem)

    # dodjeljivanje svojstava sinusnom namotu
    sin.generate_sin_windings(problem)

    # dodjeljivanje svojstava kosinusnom namotu
    cos.generate_cos_windings(problem)

    #test.test_windings(problem)






