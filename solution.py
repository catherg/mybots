import numpy
import pyrosim.pyrosim as pyrosim
import os
import sys
import random
import constants as c
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = (numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * c.numMotorNeurons) - 1
        #print("WEIGHTS:",  self.weights, "\n")
        
       # self.weights = self.weights * c.numMotorNeurons - 1


    def Start_Simulation(self, mode):
        self.Create_Brain()
        self.Create_Body()
        os.system("python3 simulate.py " + mode +  " " + str(self.myID) + " 2&>1 &")
        #print("SIMULATION CREATED!!!!")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+ str(self.myID) + ".txt"):
            time.sleep(0.1)
        f = open("fitness"+ str(self.myID) + ".txt", "r")
        line = f.read()
        if line != '\n':
            #print("READING:",line, "end of reading")
            self.fitness = float(line)
        f.close()
        os.system("rm " + "fitness"+ str(self.myID) + ".txt")

    def Create_World():
        pyrosim.Start_SDF("world.sdf")
       ## pyrosim.Send_Cube(name="Box", pos=[-2,-2,z] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        cube_pos = [0,0,1]
        joint_pos = [1.5,0,1]

        for i in range(c.numSensorNeurons):
            ## figure
            cube_pos[0] += 1.5
            pyrosim.Send_Cube(name= "cube" + str(i), pos=cube_pos , size=[3,1,1])
            if i > 0:
                ## figure out pos
                joint_pos = cube_pos
                joint_pos[0] += 1.5
                pyrosim.Send_Joint(name = str(i - 1) + "_" + str(i), parent= str(i - 1) , child = str(i) , type = "revolute", position =joint_pos, jointAxis = "1 0 0")


        

        pyrosim.End()


    def Create_Brain(self):
        
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
        for i in range(c.numSensorNeurons):
            pyrosim.Send_Sensor_Neuron(name = i, linkName = "cube" + str(i))

        increment = 1
        for j in range(c.numSensorNeurons, c.numSensorNeurons + c.numMotorNeurons):
            pyrosim.Send_Motor_Neuron(name = j , jointName = str(increment - 1) + "_" + str(increment))
            increment = increment + 1

        #pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        #pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Leftleg")
        #pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Rightleg")
        #pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        #pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        #pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg")
        #pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftLowerLeg")
        #pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_Backleg")
        #pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_Frontleg")
        #pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_Leftleg")
        #pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_Rightleg")
        #pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Frontleg_FrontLowerLeg")
       # pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Backleg_BackLowerLeg")
        #pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Rightleg_RightLowerLeg")
        #pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Leftleg_LeftLowerLeg")
    
        for currentRow in range(0,c.numSensorNeurons):
            for currentColumn in range(0,c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons ,
                weight = self.weights[currentRow, currentColumn])

        pyrosim.End()

        
    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons - 1)
        randomColumn = random.randint(0,c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * c.numMotorNeurons - 1

    def Set_ID(self, uniqueID):
        self.myID = uniqueID


        