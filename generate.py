import pyrosim.pyrosim as pyrosim
import random

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    #pyrosim.Send_Cube(name="Box", pos=[-2,-2,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    #pyrosim.Start_URDF("body.urdf")
    #pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
    #pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [2,0,1])
    #pyrosim.Send_Cube(name="Backleg", pos=[0.5,0,-0.5] , size=[length,width,height])
    #pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [1,0,1])
    #pyrosim.Send_Cube(name="Frontleg", pos=[-0.5,0,-0.5] , size=[length,width,height])
    #pyrosim.End()

    pass

def Generate_Body():
   # pyrosim.Start_SDF("world.sdf")
   # pyrosim.Send_Cube(name="Box", pos=[-2,-2,z] , size=[length,width,height])
   # pyrosim.End()
    #pyrosim.Start_URDF("body.urdf")
    #pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
    #pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [2,0,1])
    #pyrosim.Send_Cube(name="Backleg", pos=[0.5,0,-0.5] , size=[length,width,height])
    #pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [1,0,1])
    #pyrosim.Send_Cube(name="Frontleg", pos=[-0.5,0,-0.5] , size=[length,width,height])
    #pyrosim.End()
    pass

def Generate_Brain():
    #pyrosim.Start_NeuralNetwork("brain.nndf")
    #pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
    #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
    #pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
    #pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
   # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 0.0 )
   # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 0.1 )
   # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -4.0 )
   # pyrosim.Send_Synapse( sourceNeuronName = 3 , targetNeuronName = 1 , weight = 0.0 )
   # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 0.0 )



    #for i in range(0,3):
    #    for j in range(3,5):
    #        used_weight = -1 + 2 * random.random()
    #        pyrosim.Send_Synapse(sourceNeuronName = i , targetNeuronName = j , weight = used_weight)
    #        print("WEIGHT: ", used_weight)

    pyrosim.End()


    



Create_World()
#Create_Robot()
Generate_Body()
Generate_Brain()


# for k in range(0,5):
#     z = 0.5
#     length = 1
#     width = 1
#     height = 1
#     for j in range(0,5):
#         z = 0.5
#         length = 1
#         width = 1
#         height = 1
#         for i in range(0,10):
#             length = 0.9 * length
#             width = 0.9 * width
#             height = 0.9 * height
#             pyrosim.Send_Cube(name="Box", pos=[k,j,z] , size=[length,width,height])
#             z = z + height