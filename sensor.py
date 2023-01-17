import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)

    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save('data/backLegSensor.npy', self.values, allow_pickle = True, fix_imports = True)
       ## numpy.save('data/frontLegSensor.npy', self.values, allow_pickle = True, fix_imports = True)