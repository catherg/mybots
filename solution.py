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
        #self.weights = (numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * c.numMotorNeurons) - 1
        self.weights = []
        self.sensors = []
        self.joints = []
        self.cubepositions = {}
        self.jointpositions = {}
        self.randomaxis = {}
        self.sizes = {}
        self.links = c.numLinks - 1
        self.axis_array = [[] for j in range(c.numLinks - 1)] 
        
       # self.weights = self.weights * c.numMotorNeurons - 1


    def Start_Simulation(self, mode):
        self.Create_Body()
        self.Create_Brain()
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
        pyrosim.Start_URDF(f"body{self.myID}.nndf")
        cube_pos = [0,0,0]
        cube_size = [1, 1, 1]
        rand_x = 0
        rand_y = 0
        rand_z = 0
        color_find = 0       
        for i in range(c.numLinks):
            rand_x = numpy.random.uniform(1,3)
            rand_y = numpy.random.uniform(1,3)
            rand_z = numpy.random.uniform(1,3)
            color_find = numpy.random.randint(0,2)
            cube_size = [rand_x, rand_y, rand_z]
            self.sizes[i] = cube_size
            rand_axis = numpy.random.randint(0,3)
            cube_pos = [0,0,0]
            if i == 0:
                cube_pos[2] = rand_z / 2
                pyrosim.Send_Cube(name="Torso", pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                self.sensors.append([i, "Torso"])
            else:
                cube_pos[rand_axis] = cube_size[rand_axis] / 2
                if color_find == 1:
                    pyrosim.Send_Cube(name="Leg" + str(i), pos=cube_pos , size=cube_size, color_name = "Green", color_string = "0 180.0 0.0 1.0")
                    self.sensors.append([i, "Leg" + str(i)])
                else:
                    pyrosim.Send_Cube(name="Leg" + str(i), pos=cube_pos , size=cube_size, color_name = "Blue", color_string = "0 1.0 1.0 1.0") 
                self.randomaxis[i - 1] = rand_axis       
            self.cubepositions[i] = cube_pos
    ############## ---------- CREATING JOINT POSITIONS  ---------------- #################
     ### choose a random previous joint from the dictionaries
    # grab the previous axis to that joint position and the axis of that joint position
    # change the cube position to reflect that, and then record that as the new joint position
        prev_joint = 0
        self.axis_array = [[] for j in range(c.numLinks - 1)]
        self.jointpositions = {}
        self.joints = []
        #### first absolute joint created ####
        curr_size = self.sizes[0]
        joint_pos = self.cubepositions[0]
        joint_pos[self.randomaxis[0]] += curr_size[self.randomaxis[0]] / 2
        pyrosim.Send_Joint(name = "Torso_Leg1" , parent= "Torso" , child = "Leg1" , type = "revolute", position = joint_pos, jointAxis = "1 0 0")
        self.joints.append([0, "Torso_Leg1"])
        self.jointpositions[0] = joint_pos
        self.axis_array[0].append(self.randomaxis[0])
        print("AXIS ARRAY:", self.randomaxis)
        for j in range(1, c.numMotorNeurons):
            prev_joint = numpy.random.randint(0,j + 1)
            while self.randomaxis[j] in self.axis_array[prev_joint]:
                prev_joint = numpy.random.randint(0,j + 1)
            curr_size = self.sizes[prev_joint + 1]
            joint_pos = self.cubepositions[prev_joint + 1]
            print("JOINT POSITION1:", joint_pos)
            joint_pos[self.randomaxis[j]] += curr_size[self.randomaxis[j]] / 2
            print("JOINT POSITION2:", joint_pos)
            self.axis_array[prev_joint].append(self.randomaxis[j])
            if prev_joint == 0:
                pyrosim.Send_Joint(name = "Torso_Leg" + str(j + 1), parent= "Torso" , child = "Leg" + str(j + 1) ,
                type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                self.joints.append([j, "Torso_Leg" + str(j + 1)])          
            else:
                pyrosim.Send_Joint(name = "Leg" + str(prev_joint) + "_Leg" + str(j + 1), parent= "Leg" + str(prev_joint) , child = "Leg" + str(j + 1) ,
                type = "revolute", position = joint_pos, jointAxis = "1 0 0")
                self.joints.append([j, "Leg" + str(prev_joint) + "_Leg" + str(j + 1)])          
            self.jointpositions[j] = joint_pos
        pyrosim.End()
        self.weights = (numpy.random.rand(len(self.sensors),c.numMotorNeurons) * c.numMotorNeurons) - 1

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) + ".nndf")
        increment = 0
        for i in self.sensors:
            pyrosim.Send_Sensor_Neuron(name = increment , linkName = i[1])
            increment += 1    
        increment = len(self.sensors)
        print("JOINTS:", self.joints)
        for j in self.joints:
            pyrosim.Send_Motor_Neuron( name = increment , jointName = j[1])          
            increment += 1
    
        for currentRow in range(len(self.sensors)):
            for currentColumn in range(len(self.joints)):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + len(self.sensors),
                weight = self.weights[currentRow, currentColumn])
        pyrosim.End()
       
    def Mutate(self):
        if len(self.sensors) > 1:
            randomRow = random.randint(0,len(self.sensors) - 1)
            randomColumn = random.randint(0,len(self.joints) - 1)
            self.weights[randomRow, randomColumn] = random.random() * len(self.joints) - 1

    def Set_ID(self, uniqueID):
        self.myID = uniqueID

    ### mutate body adds a leg to a random axis
    def Mutate_Body(self):
        pass






        