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
        #self.numSensors = numpy.random.randint(2, c.numLinks)
        #self.numMotors = self.numSensors - 1
        #self.cubepositions = {}
        self.first_y = 0
        self.ylength = {}
        #self.weights = (numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * c.numMotorNeurons) - 1
        self.weights = []
        self.sensors = []
        self.joints = []
        self.torso_size = []
        self.legs = [[],[],[],[]]
        self.cubepositions = {}
        self.leg_height = 0
        
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
        #pyrosim.Start_SDF("world.sdf")
       ## pyrosim.Send_Cube(name="Box", pos=[-2,-2,z] , size=[length,width,height])
        #pyrosim.End()
        pass

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        
        cube_pos = [0,0,0]
        cube_size = [1, 1, 1]
        rand_x = numpy.random.uniform(2,6)
        rand_y = numpy.random.uniform(2,6)
        rand_z = numpy.random.uniform(1,4)
        color_find = numpy.random.randint(0,2)
        cube_size = [rand_x, rand_y, rand_z]
        self.leg_height = numpy.random.uniform(1,6)

        self.torso_size = [rand_x / 2, rand_y / 2, rand_z / 2]

        ###### --------- Section For Torso Creation ----------- ############### 
        cube_pos[2] =  self.torso_size[2] + (self.leg_height)
        self.cubepositions[0] = cube_pos
        if color_find == 1:
            pyrosim.Send_Cube(name="Torso", pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
            self.sensors.append([0, "Torso"])
        else:
            pyrosim.Send_Cube(name="Torso", pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0") 


        ### ------- section for Leg Creation -------- #####

        self.legs = [[-self.torso_size[0], self.torso_size[1], self.leg_height],
                      [self.torso_size[0], self.torso_size[1], self.leg_height],
                    [-self.torso_size[0], -self.torso_size[1], self.leg_height],
                      [self.torso_size[0], -self.torso_size[1], self.leg_height]]
        
        rand_x = numpy.random.uniform(0.2,2)
        rand_y = numpy.random.uniform(0.2,2)
        #rand_z = numpy.random.uniform(1,3)
        cube_size = [rand_x, rand_y, self.leg_height]


        for i in range(1,5): 
            color_find = numpy.random.randint(0,2)
            cube_pos = [0,0,-(cube_size[2] / 2)]
            self.cubepositions[i] = cube_pos    
            if color_find == 1:
                pyrosim.Send_Cube(name="Leg" + str(i), pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                self.sensors.append([i, "Leg" + str(i)])
            else:
                pyrosim.Send_Cube(name="Leg" + str(i), pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0")   

 
        #### ----------- Section for Head Creation ---------- #####

        rand_x = numpy.random.uniform(2,4)
        rand_y = numpy.random.uniform(2,4)
        rand_z = numpy.random.uniform(1,3)
        color_find = numpy.random.randint(0,2)
        cube_size = [rand_x, rand_y, rand_z]

        cube_pos = [(cube_size[0] / 2), 0, (cube_size[2] / 2)]

        self.cubepositions[5] = cube_pos
    
        if color_find == 1:
            pyrosim.Send_Cube(name="Head", pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
            self.sensors.append([5, "Head"])
        else:
             pyrosim.Send_Cube(name="Head", pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0") 
      
            
    ######## CREATING JOINTS NOW #########

        joint_pos = [0,0,0]
        ## ------ creating the leg joints ----------- ######
        for j in range(1,5):
            joint_pos = self.legs[j - 1]
            #joint_pos[2] += self.leg_height
            pyrosim.Send_Joint(name = "Torso_Leg" + str(j), parent= "Torso",
            child = "Leg" + str(j), type = "revolute", position = joint_pos, jointAxis = "1 0 0")

            self.joints.append([j - 1,"Torso_Leg" + str(j)])


        #### --------- creating the head joint ---------- #######

        joint_pos = [self.torso_size[0], 0 , (2 * self.torso_size[2]) + (self.leg_height)]
        pyrosim.Send_Joint(name = "Torso_Head", parent= "Torso",
        child = "Head", type = "revolute", position = joint_pos, jointAxis = "1 0 0")

        self.joints.append([4,"Torso_Head"])


        pyrosim.End()

        self.weights = (numpy.random.rand(len(self.sensors),c.numMotorNeurons) * c.numMotorNeurons) - 1


    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")

        increment = 0
        for i in self.sensors:
            pyrosim.Send_Sensor_Neuron(name = increment , linkName = i[1])
            increment += 1    
        
        increment = len(self.sensors)
        for j in self.joints:
            pyrosim.Send_Motor_Neuron( name = increment , jointName = j[1])
            increment += 1
        
    
        for currentRow in range(len(self.sensors)):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + len(self.sensors) ,
                weight = self.weights[currentRow, currentColumn])
        

        pyrosim.End()

        
    def Mutate(self):
        if len(self.sensors) > 1:
            randomRow = random.randint(0,len(self.sensors) - 1)
            randomColumn = random.randint(0,c.numMotorNeurons - 1)
            self.weights[randomRow, randomColumn] = random.random() * c.numMotorNeurons - 1

    def Set_ID(self, uniqueID):
        self.myID = uniqueID


        