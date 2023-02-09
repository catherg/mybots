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
        self.numsensors = numpy.random.randint(1,c.numLinks)
        self.cubepositions = {}
        self.nummotors = self.numsensors - 1
        self.weights = (numpy.random.rand(self.numsensors,self.nummotors) * self.nummotors) - 1


        #print("WEIGHTS:",  self.weights, "\n")
        
       # self.weights = self.weights * c.numMotorNeurons - 1


    def Start_Simulation(self, mode):
        self.Create_Brain()
        self.Create_Body()
        os.system("python3 simulate.py " + mode +  " " + str(self.myID) + " 2&>1 &")
        
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+ str(self.myID) + ".txt"):
            time.sleep(0.1)
        f = open("fitness"+ str(self.myID) + ".txt", "r")
        line = f.read()
        if line != '\n':
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
        joint_pos = [0,0,1]
        sizing = [1,1,1]
        rand_num_x = 1
        rand_num_y = 1
        rand_num_z = 1
       
        for i in range(self.numsensors):
            rand_num_x = numpy.random.uniform(1,3)
            rand_num_y = numpy.random.uniform(1,3)
            rand_num_z = numpy.random.uniform(1,3)
            sizing = [rand_num_x, rand_num_y, rand_num_z]
            if i == 0:
                pyrosim.Send_Cube(name= "Torso0", pos=cube_pos , size=sizing)  
            else:
                cube_pos[0] += rand_num_x / 2
                pyrosim.Send_Cube(name= "Torso" + str(i), pos=cube_pos , size=sizing)

            self.cubepositions[i] = cube_pos

        print("passed")  
        for j in range(self.nummotors):
            joint_pos = self.cubepositions[j]
            joint_pos[0] += rand_num_x / 2
            pyrosim.Send_Joint(name = "Torso" + str(i) + "_" + "Torso" + str(i + 1), parent= "Torso" + str(i) ,
            child = "Torso" + str(i + 1) , type = "revolute", position =joint_pos, jointAxis = "1 0 0")

    


        pyrosim.End()


            #### check 0 or 1, if 1 make it green add it to sensor lists, if 0 then make it blue
            ### create a list for joints to add them after you have created them --> for motor neurons in create brain

    def Create_Brain(self):
        

        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")

        #print("SENSORS:", self.numsensors)

        for i in range(self.numsensors):
            pyrosim.Send_Sensor_Neuron(name = i, linkName = "Torso" + str(i))
            #print("Torso" + str(i))


        increment = 0
        #print("SENSORS - MOTOR RANGE:")
        for j in range(self.numsensors, (self.numsensors + self.nummotors)):
            pyrosim.Send_Motor_Neuron(name = j , jointName = "Torso" + str(increment) + "_" + "Torso" + str(increment + 1))
            #print("Torso" + str(increment) + "_" + "Torso" + str(increment + 1))
            increment = increment + 1
            

        #pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")p  
        #pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_Backleg")
    ###******************
        for currentRow in range(0,self.numsensors):
            for currentColumn in range(0,self.nummotors):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons ,
                weight = self.weights[currentRow, currentColumn])

        pyrosim.End()

        
    def Mutate(self):
        
        randomRow = random.randint(0,self.numsensors - 1)
        randomColumn = random.randint(0,self.nummotors - 1)
        self.weights[randomRow, randomColumn] = random.random() * self.nummotors - 1

    
        

    def Set_ID(self, uniqueID):
        self.myID = uniqueID


        