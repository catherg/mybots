import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import constants as c
from world import WORLD
from robot import ROBOT
from pyrosim.neuralNetwork import NEURAL_NETWORK

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.solutionID = solutionID
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        #pyrosim.Prepare_To_Simulate(self.robotId)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        for i in range(0, 1000):
            self.robot.Sense()
            self.robot.Think()
            self.robot.Act()
            p.stepSimulation()
            time.sleep(c.sleep)

    def __del__(self):
        p.disconnect() 

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)