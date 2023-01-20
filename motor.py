import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
    #    self.Prepare_To_Act()

   # def Prepare_To_Act(self):
    #    self.amplitude = c.amplitude
    #    self.frequency = c.frequency
    #    self.phaseOffset = c.phaseOffset
    #   if self.jointName == "Torso_Backleg":
    #        self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 1000, num=1000) + self.phaseOffset)
    #    else:
    #        self.motorValues = self.amplitude * numpy.sin(0.5 * self.frequency * numpy.linspace(0, 1000, num=1000) + self.phaseOffset)



    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,

        jointName = self.jointName,

        controlMode = p.POSITION_CONTROL,

        targetPosition = desiredAngle,

        maxForce = c.maxForce)
    
   # def Save_Values(self):
    #    numpy.save('data/targetAngle.npy', self.motorValues, allow_pickle = True, fix_imports = True)
