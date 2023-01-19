import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-2,-2,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="Backleg", pos=[0.5,0,-0.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="Frontleg", pos=[-0.5,0,-0.5] , size=[length,width,height])
    pyrosim.End()
def Generate_Body():



Create_World()
Create_Robot()


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