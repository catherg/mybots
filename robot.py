import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import os
class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+ solutionID +".nndf")
        os.system("rm " + "brain"+ solutionID +".nndf")



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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                ##print("first_act:",type(jointName))
                self.motors[jointName].Set_Value(self.robotId, desiredAngle * c.motorJointRange)
           #     print(neuronName, jointName, desiredAngle)
       ## t = 0
       ## for jointName in pyrosim.jointNamesToIndices:
        ##    self.motors[jointName].Set_Value(self.robotId, t)
        ##    t = t + 1
    def Think(self):

        self.nn.Update()
        ##self.nn.Print()
    
    def Get_Fitness(self,solutionID):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        os.system("mv " + "tmp" + str(solutionID) + ".txt fitness" + str(solutionID) + ".txt")
        f.close()