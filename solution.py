import numpy
import pyrosim.pyrosim as pyrosim
import os
import random

class SOLUTION:
    def __init__(self):
        self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()],
        [numpy.random.rand(), numpy.random.rand()]])
        self.weights = self.weights * 2 - 1

    def Evaluate(self, mode):
        self.Create_Brain()
        os.system("python3 simulate.py " + mode)
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Create_World():
        pyrosim.Start_SDF("world.sdf")
       ## pyrosim.Send_Cube(name="Box", pos=[-2,-2,z] , size=[length,width,height])
        pyrosim.End()

    def Create_Body():
        pyrosim.Start_URDF("body.urdf")
      ##  pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
      ##  pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [2,0,1])
      ##  pyrosim.Send_Cube(name="Backleg", pos=[0.5,0,-0.5] , size=[length,width,height])
      ##  pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [1,0,1])
      ##  pyrosim.Send_Cube(name="Frontleg", pos=[-0.5,0,-0.5] , size=[length,width,height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
  
        for currentRow in range(0,3):
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 ,
                 weight = self.weights[currentRow, currentColumn])

        pyrosim.End()
    
    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

        