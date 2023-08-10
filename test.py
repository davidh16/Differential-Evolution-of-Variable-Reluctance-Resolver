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

x = [69.45828864, 6.35603092, 11.92826483, 35.25952005, 1.65654843, 4.39390028, 9.07008962, 69.63825479, 2.54907215]

"""

bounds : [(33, 180), (5, 10), (5, 20), (10, 105), (-0.5, 3.5), (2, 5), (2, 168), (10, 120), (-0.5, 3.5)]

"""
"""
[61.6092931, 6.18938252, 13.9443661, 87.6483885, 0.0128315008, 2.88579374, 28.4927912, 28.8945113, 2.11261638]
[156.98131624, 8.97027104, 9.03393075, 10.54542967, 0.51870268, 2.07271165, 4.52710827, 17.02201235, 0.34864748]
[173.40459608, 8.97027104, 17.20963399, 10.54542967, 0.51870268, 2.54540067, 4.52710827, 118.37916181, 0.44619824]
[116.676391, 6.91213058, 16.864820, 90.449532, -0.0490687208, 4.07455876, 5.47901980, 117.838242, 0.457307249]
[112.68493716, 6.37929038, 8.03058763, 29.85407647, 3.40251679, 4.02000953, 5.59148995, 47.60697073, 0.95148829]
[133.45364822, 7.44500424, 18.29047036, 29.22957559, 2.50357857, 4.59058454, 8.9274638, 53.00177489, 1.90902377]
[128.24281921, 5.90109176, 18.29047036, 29.22957559, 2.50357857, 4.59058454, 29.18074357, 53.00177489, 3.12059265]
[171.76496846, 5.74228312, 5.7585698, 29.97199236, 3.33908427, 3.29815807, 12.73484054, 51.79179695, 1.06370178]
[134.03828463, 6.16952899, 5.7227577, 29.46610285, 2.73886346, 3.80826133, 20.14612509, 98.80272895, 0.98637161]
[162.30555797, 6.41224636, 16.60154732, 28.92446958, 2.96814168, 3.99556531, 17.82922763, 54.41220883, 2.52966435]
[160.14865396, 6.92792534, 8.95743257, 29.77900801, 2.89816645, 2.67473093, 19.57781567, 95.76824123, 0.64274977]
[123.39716692, 7.30886453, 5.79439946, 29.71346274, 2.82038527, 2.92376222, 31.48534844, 66.09354876, 2.31240442]
[142.528377, 7.66979817, 5.66934963, 18.7165563, 2.91674056, 3.99452496, 2.61509642, 50.7773443, -0.0832466281]
[168.62579152, 5.99427851, 12.84345008, 29.2674852, 2.76698363, 2.3267821, 29.68075176, 64.52325709, 1.8691914]
[165.60647299, 8.15549123, 10.26114413, 23.72484442, 0.75823601, 2.31965533, 2.71119004, 65.5248117, 0.48160911]
[77.37546004, 8.13135999, 15.79102929, 27.6108778, 2.8632418, 3.12861621, 8.04882914, 78.53471918, 2.31577227]
[172.57966364, 7.11750461, 12.04145018, 28.95356814, 2.65394265, 3.01474823, 24.74906067, 45.96202243, 0.73283035]
[165.38407771, 5.81650629, 12.41089934, 29.5062183, 3.11280107, 3.02272742, 37.59687882, 31.43481809, 1.20115259]
[179.7378074, 6.95130263, 8.8420612, 29.34772487, 2.99646583, 3.62491801, 16.50669202, 65.84013867, 0.73073548]
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