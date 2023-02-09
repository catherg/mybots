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
        self.xlength = {}
        #self.weights = (numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * c.numMotorNeurons) - 1
        self.weights = []
        self.sensors = []
        self.joints = []
        
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
            print("READING:",line, "end of reading")
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
        cube_size = [1, 1, 1]
        rand_x = numpy.random.uniform(1,3)
        rand_y = numpy.random.uniform(1,3)
        rand_z = numpy.random.uniform(1,3)
        self.cubepositions = {}
        self.xlength = {}
        color_find = numpy.random.randint(0,2)

        for i in range(c.numLinks):
            rand_x = numpy.random.uniform(1,3)
            rand_y = numpy.random.uniform(1,3)
            rand_z = numpy.random.uniform(1,3)
            color_find = numpy.random.randint(0,2)
            cube_size = [rand_x, rand_y, rand_z]
            if i == 0:
                cube_pos[1] = rand_y / 2
                if color_find == 1:
                    pyrosim.Send_Cube(name="Torso", pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                    self.sensors.append([i, "Torso"])
                else:
                    pyrosim.Send_Cube(name="Torso", pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0")
                
            
            else:
                cube_pos[0] = rand_x / 2
                if color_find == 1:
                    pyrosim.Send_Cube(name="Torso" + str(i), pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                    self.sensors.append([i, "Torso" + str(i)])
                else:
                    pyrosim.Send_Cube(name="Torso" + str(i), pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0")       

            self.cubepositions[i] = cube_pos
            self.xlength[i] = rand_x

        joint_pos = [0,0,1]
        for j in range(c.numMotorNeurons):
            if j == 0:
                joint_pos = self.cubepositions[j]
                joint_pos[0] = self.xlength[j] / 2
                pyrosim.Send_Joint(name = "Torso_Torso1" , parent= "Torso" , child = "Torso1" ,
                type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                self.joints.append([j, "Torso_Torso1"])
            else:
                joint_pos = self.cubepositions[j]
                joint_pos[0] = self.xlength[j] / 2
                pyrosim.Send_Joint(name = "Torso" + str(j) + "_" + "Torso" + str(j + 1), parent= "Torso" + str(j) ,
                child = "Torso" + str(j + 1), type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                self.joints.append([j,"Torso" + str(j) + "_" + "Torso" + str(j + 1)])
            

        print("number of links:", c.numLinks)
        print("SENSOR DICTIONARY:", self.sensors, "length:", len(self.sensors))
        """

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])
        pyrosim.Send_Cube(name="Backleg", pos=[0,-0.5,0] , size=[0.2,1,0.2]) 
        pyrosim.Send_Cube(name="Frontleg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Cube(name="Leftleg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Cube(name="Rightleg", pos=[0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint(name = "Backleg_BackLowerLeg" , parent= "Backleg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Frontleg_FrontLowerLeg" , parent= "Frontleg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Rightleg_RightLowerLeg" , parent= "Rightleg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "Leftleg_LeftLowerLeg" , parent= "Leftleg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        
        """

        pyrosim.End()

        self.weights = (numpy.random.rand(len(self.sensors),c.numMotorNeurons) * c.numMotorNeurons) - 1


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")

        """       
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Leftleg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Rightleg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_Frontleg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_Leftleg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_Rightleg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Frontleg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Backleg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Rightleg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Leftleg_LeftLowerLeg")

        """
        increment = 0
        for i in self.sensors:
           # if i[0] == 0:
            #    pyrosim.Send_Sensor_Neuron(name = i[0] , linkName = "Torso")
            #    print(i[0], i[1])
            #else:
            pyrosim.Send_Sensor_Neuron(name = increment , linkName = i[1])
            print(increment, i[1])
            increment += 1
        
        increment = 1
        for j in range(len(self.sensors), (len(self.sensors) + c.numMotorNeurons)):
            if j == len(self.sensors):
                pyrosim.Send_Motor_Neuron( name = j , jointName = "Torso_Torso1")
                print(j, "Torso_Torso1")
            else:
                pyrosim.Send_Motor_Neuron( name = j , jointName = "Torso" + str(increment) + "_" + "Torso" + str(increment + 1))
                print(j, "Torso" + str(increment) + "_" + "Torso" + str(increment + 1))
                increment += 1
    




    
        for currentRow in range(len(self.sensors)):
            for currentColumn in range(c.numMotorNeurons):
                print("row:", currentRow, "column:", currentColumn)
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + len(self.sensors) ,
                weight = self.weights[currentRow, currentColumn])
                print("weight:", self.weights[currentRow, currentColumn])

        pyrosim.End()

        
    def Mutate(self):
        if len(self.sensors) > 1:
            randomRow = random.randint(0,len(self.sensors) - 1)
            randomColumn = random.randint(0,c.numMotorNeurons - 1)
            self.weights[randomRow, randomColumn] = random.random() * c.numMotorNeurons - 1

    def Set_ID(self, uniqueID):
        self.myID = uniqueID


        