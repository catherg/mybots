import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = -1
y = -1
z = 0.5

for k in range(0,5):
    z = 0.5
    length = 1
    width = 1
    height = 1
    for j in range(0,5):
        z = 0.5
        length = 1
        width = 1
        height = 1
        for i in range(0,10):
            length = 0.9 * length
            width = 0.9 * width
            height = 0.9 * height
            pyrosim.Send_Cube(name="Box", pos=[k,j,z] , size=[length,width,height])
            z = z + height
    
pyrosim.End()
