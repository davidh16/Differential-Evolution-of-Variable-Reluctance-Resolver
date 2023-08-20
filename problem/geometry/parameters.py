import math

""""
vektor sa parametrima senzora
x = [
      vanjski_promjer_statora,
      debljina_jarma_statora, 
      duljina_pola_statora, 
      duljina_zracnog_raspora,
      duljina_pola_rotora,
      broj_polova_rotora
     ]

     primjer : x = [100, 20, 5, 30, 3]
"""

def init_stator_parameters(self, x):
    # Vanjski promjer statora
    self.Rv = x[0]

    # Debljina jarma satora u mm:
    self.Jt = x[1]

    # Duljina pola statora
    self.Sp = x[2]

    # Promjeri statora:
    self.rs1 = self.Rv - self.Jt
    self.rs2 = self.rs1 - self.Sp

    # Broj polova statora
    self.Ps = 12

    o = 2 * math.pi * self.rs2
    pal = o / 12
    pa = (pal/2)*1.5/self.rs2
    gore = pa*self.rs1
    duljina_pola = (2*math.pi*self.rs1-self.Ps*gore)/self.Ps
    kut_pola = math.degrees(duljina_pola/self.rs1)

    # Kut pola statora
    self.alS1 = kut_pola

    # Kut izmedju polova statora
    self.kutS = (360 - self.Ps * self.alS1) / self.Ps

    self.sn = 0.2 * self.rs1 * math.sin(math.radians(self.alS1 / 2))

def init_rotor_parameters(self, x):
    # Debljina zracnog raspora:
    self.DZ = x[3]

    # Broj polova rotora

    broj_polova_rotora = [2, 3, 4, 5, 6]

    self.Pr = broj_polova_rotora[round(x[4])]

    # Promjeri rotora:
    self.rr1 = self.rs2 - self.DZ
    self.rr2 = self.rr1 - 0.1*self.rr1

    # Kut pola rotora:
    if self.Pr != 2:
        self.alR1 = 360/self.Pr
    else:
        self.alR1 = 45

    # Kut izmedju polova rotora
    self.alR3 = 360 / self.Pr - self.alR1

    # polumjer osovine
    self.rV = self.rr2 * 1 / 3