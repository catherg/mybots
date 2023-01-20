import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import constants as c
from world import WORLD
from robot import ROBOT
from pyrosim.neuralNetwork import NEURAL_NETWORK

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        #pyrosim.Prepare_To_Simulate(self.robotId)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(0, 1000):
            self.robot.Sense()
            self.robot.Think()
            self.robot.Act()
            #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
 #   frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")

            p.stepSimulation()
            time.sleep(c.sleep)
    def __del__(self):
        p.disconnect()  