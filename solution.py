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
        self.xlength = []
        self.ylength = []
        self.zlength = []
        self.xtrack = 0
        self.ytrack = 0
        self.ztrack = 0
        #self.weights = (numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * c.numMotorNeurons) - 1
        self.weights = []
        self.sensors = []
        self.joints = []
        self.cubepositions = {}
        self.randomaxis = {}
        self.sizes = {}
       
        
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
        
        cube_pos = [0,0,0]
        cube_size = [1, 1, 1]
        rand_x = numpy.random.uniform(1,3)
        rand_y = numpy.random.uniform(1,3)
        rand_z = numpy.random.uniform(1,3)
        color_find = numpy.random.randint(0,2)
        rand_axis = numpy.random.randint(0,3)
        
        for i in range(c.numLinks):
            rand_x = numpy.random.uniform(1,3)
            rand_y = numpy.random.uniform(1,3)
            rand_z = numpy.random.uniform(1,3)
            color_find = numpy.random.randint(0,2)
            cube_size = [rand_x, rand_y, rand_z]
            self.sizes[i] = cube_size
            if i == 0:
                cube_pos[2] = rand_z / 2
                self.cubepositions[i] = cube_pos
                if color_find == 1:
                    pyrosim.Send_Cube(name="Torso", pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                    self.sensors.append([i, "Torso"])
                else:
                    pyrosim.Send_Cube(name="Torso", pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0")
                rand_axis = 3
    ###### ------- CREATING BLOCKS FOR THE Y AXIS --------- ########
            elif rand_axis == 1:
                cube_pos[1] = rand_y / 2
                self.cubepositions[i] = cube_pos
                if color_find == 1:
                    pyrosim.Send_Cube(name="Cubey" + str(self.ytrack), pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                    self.sensors.append([i, "Cubey" + str(self.ytrack)])
                else:
                    pyrosim.Send_Cube(name="Cubey" + str(self.ytrack), pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0") 
                #self.ylength.append(rand_y)
                self.ytrack += 1
    #### ------- CREATING BLOCKS FOR THE X AXIS --------- ########
            elif rand_axis == 0:
                cube_pos[0] = rand_x / 2
                self.cubepositions[i] = cube_pos
                if color_find == 1:
                    pyrosim.Send_Cube(name="Cubex" + str(self.xtrack), pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                    self.sensors.append([i, "Cubex" + str(self.xtrack)])
                else:
                    pyrosim.Send_Cube(name="Cubex" + str(self.xtrack), pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0") 
                #self.xlength.append(rand_x)
                self.xtrack += 1
    ##### ------- CREATING BLOCKS FOR THE Z AXIS --------- ######## 
            elif rand_axis == 2:
                cube_pos[2] = rand_z / 2
                self.cubepositions[i] = cube_pos
                if color_find == 1:
                    pyrosim.Send_Cube(name="Cubez" + str(self.ztrack), pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                    self.sensors.append([i, "Cubez" + str(self.ztrack)])
                else:
                    pyrosim.Send_Cube(name="Cubez" + str(self.ztrack), pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0") 
                #self.zlength.append(rand_z)
                self.ztrack += 1

            cube_pos = [0,0,0]
            self.randomaxis[i] = rand_axis           
    ############## ---------- CREATING JOINT POSITIONS  ---------------- #################
        joint_pos = [0,0,0]
        x_track = 0
        y_track = 0
        z_track = 0
        most_recent = "cube"      
        for j in range(c.numMotorNeurons):
            joint_pos = self.cubepositions[j]
            if j == 0:
                if self.randomaxis[j + 1] == 0:
                    joint_pos[0] += self.sizes[j][0] / 2
                    pyrosim.Send_Joint(name = "Torso_Cubex0" , parent= "Torso" , child = "Cubex0" ,
                    type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                    self.joints.append([j, "Torso_Cubex0"])
                    x_track += 1
                    most_recent = "Cubex0"
                elif self.randomaxis[j + 1] == 1:
                    joint_pos[1] += self.sizes[j][1] / 2
                    pyrosim.Send_Joint(name = "Torso_Cubey0" , parent= "Torso" , child = "Cubey0" ,
                    type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                    self.joints.append([j, "Torso_Cubey0"])
                    y_track += 1
                    most_recent = "Cubey0"
                elif self.randomaxis[j + 1] == 2:
                    joint_pos[2] += self.sizes[j][2] / 2
                    pyrosim.Send_Joint(name = "Torso_Cubez0" , parent= "Torso" , child = "Cubez0" ,
                    type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                    self.joints.append([j, "Torso_Cubez0"])
                    z_track += 1
                    most_recent = "Cubez0"
            else:
                if self.randomaxis[j + 1] == 0:
                    joint_pos[0] += self.sizes[j][0] / 2
                    pyrosim.Send_Joint(name = most_recent + "_Cubex" + str(x_track), parent= most_recent , child = "Cubex" + str(x_track) ,
                    type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                    self.joints.append([j, most_recent + "_Cubex" + str(x_track)])
                    most_recent = "Cubex" + str(x_track)
                    x_track += 1
                elif self.randomaxis[j + 1] == 1:
                    joint_pos[1] += self.sizes[j][1] / 2
                    pyrosim.Send_Joint(name = most_recent + "_Cubey" + str(y_track), parent= most_recent , child = "Cubey" + str(y_track) ,
                    type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                    self.joints.append([j, most_recent + "_Cubey" + str(y_track)])
                    most_recent = "Cubey" + str(y_track)
                    y_track += 1
                elif self.randomaxis[j + 1] == 2:
                    joint_pos[2] += self.sizes[j][2] / 2
                    pyrosim.Send_Joint(name = most_recent + "_Cubez" + str(z_track), parent= most_recent , child = "Cubez" + str(z_track) ,
                    type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                    self.joints.append([j, most_recent + "_Cubez" + str(z_track)])
                    most_recent = "Cubez" + str(z_track)
                    z_track += 1
     
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


        