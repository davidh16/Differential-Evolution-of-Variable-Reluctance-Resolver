from problem.objective_function import FC

"""

Ovaj file je namjenjen za testiranje. 
Kada bi main funckija izbacila error za određeni vektor, 
taj isti vektor bih ubacio ovdje i zakomentirao bih dio u objective_function koji se odnosi na analizu. 
Na taj način funkcija samo nacrta geometriju, a ne radi analizu te se onda može vidjeti što je pošlo po krivu tijekom crtanja geometrije.
Korištenjem ovog file-a sam debugirao sve probleme na koje sam naišao.
U komentarima su zapisani primjeri vektora koji su stvarali probleme, no ti isti problemi su riješeni.

Usage : odrediti vektor x, otkomentirati liniju 30, pokrenuti test.py

"""

#x = [167.0292834, 7.38816166, 14.54937817, 38.53294057, 3.00000026, 4.26139388, 41.14000874, 38.41421015, 3.70752308]

#x  = [100, 20, 5, 30, 6, 3, 5, 60, 3]

#x = [125.8212344, 8.17046908, 14.62579518, 27.59782459, 6.0, 4.12884229, 18.82740725, 23.43702363, 5.0]

#x = [126.42328681, 5.93482018, 6.5517732, 40.36821638, 6.00000000, 4.25860395, 5.89112131, 29.83084273, 5.00000000]
# TypeError: '>=' not supported between instances of 'float' and 'NoneType'

#x = [33.86857431, 5.59496457, 14.16791286, 28.47118468, 6.0, 3.03210196, 3.81487486, 34.00236909, 5.0]
# namoti nisu nacrtani


# FC(x)