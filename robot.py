import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def return_Sensor(self):
        return self.sensors

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self):   
        t = 0
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t)
            t = t + 1
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        t = 0
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Set_Value(self.robotId, t)
            t = t + 1
    