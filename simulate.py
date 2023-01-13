import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
import numpy
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
sleep = 1/60
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(10000)
print(backLegSensorValues)
exit()
for i in range(0, 1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    print(backLegTouch)
    time.sleep(sleep)
p.disconnect()