import math

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
    # Kut pola statora
    self.alS1 = x[3]
    self.alS2 = ((2 * math.degrees(math.asin(math.sin(math.radians(self.alS1 / 2)) * (self.rs1) / (self.rs2))  )) / self.alS1) * self.alS1
    # Broj polova statora
    self.Ps = x[4]
    # Kut izmedju polova statora
    self.kutS = (360 - self.Ps * self.alS1) / self.Ps

    self.sn = 0.2 * self.rs1 * math.sin(math.radians(self.alS1 / 2))

def init_rotor_parameters(self, x):
    # Debljina zracnog raspora:
    self.DZ = x[5]
    # Broj polova rotora
    self.Pr = x[8]
    # Duljina pola rotora:
    self.Sr = x[6]
    # Promjeri rotora:
    self.rr1 = self.rs2 - self.DZ
    self.rr2 = self.rr1 - self.Sr

    # rr1 = x[0] - x[1] - x[2] - x[5]
    # rr2 = x[0] - x[1] - x[2] - x[5] - x[6]

    # Kut pola rotora:
    self.alR1 = x[7]
    self.alR2 = 2 * math.degrees(math.asin(math.sin(math.radians(self.alR1 / 2)) * self.rr1 / self.rr2))
    self.krN = self.alR2 / self.alR1
    self.kr = self.krN
    self.alR2 = self.kr * self.alR1
    # Kut izmedju polova rotora
    self.alR3 = 360 / self.Pr - self.alR2
    # polumjer osovine
    self.rV = self.rr2 * 1 / 3