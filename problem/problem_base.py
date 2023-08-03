import femm
import problem.geometry.parameters as parameters
import problem.geometry.rotor as rotor
import problem.geometry.stator as stator
import problem.windings.windings as windings


class Problem:
    def __init__(self, x):
        self.init_stator_parameters(x)
        self.init_rotor_parameters(x)

        # po uzoru na 11BRW -300-M iz kataloga https://ecatalog.dynapar.com/downloads/HM_11_R11__DS_702922_1_.pdf

        # brzina vrtnje
        self.rpm = 1500
        # frekvencija u Hz
        self.f = 0
        # struja u mA
        self.i = 8.3e-3
        # napon u V
        self.v = 10
        # aksijalna duljina u mm
        self.axial_length = 15

        # opens femm, 1 is to hide main window
        femm.openfemm(1)

        # initializing a new document
        femm.newdocument(0)

        femm.mi_probdef(self.f, 'millimeters', 'planar', 1.e-8, self.axial_length, 30)

        # hides the floating Lua console window
        femm.hideconsole()

        # hides the floating FEMM Properties display window
        femm.hidepointprops()

    def init_stator_parameters(self, x):
        parameters.init_stator_parameters(self, x)

    def init_rotor_parameters(self, x):
        parameters.init_rotor_parameters(self, x)

    def generate_stator(self):
        stator.generate_stator(self)

    def generate_windings(self):
        windings.generate_windings(self)

    def generate_rotor(self):
        rotor.generate_rotor(self)
