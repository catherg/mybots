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
    pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0.5,1])
    pyrosim.Send_Cube(name="Link1", pos=[0,0.5,0.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,1,0])
    pyrosim.Send_Cube(name="Link2", pos=[0,0.5,-0.5] , size=[length,width,height])
    pyrosim.End()


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

    
