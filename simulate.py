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
backLegSensorValues = numpy.zeros(500)
frontLegSensorValues = numpy.zeros(500)
for i in range(0, 500):
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = "robot",

    jointName = b'Torso_Backleg',

    controlMode = p.POSITION_CONTROL,

    targetPosition = 0.0,

    maxForce = 500)
    p.stepSimulation()
    #print("back:", backLegSensorValues[i], "    front:", frontLegSensorValues[i])
    time.sleep(sleep)
numpy.save('data/backLegSensor.npy', backLegSensorValues, allow_pickle = True, fix_imports = True)
numpy.save('data/frontLegSensor.npy', frontLegSensorValues, allow_pickle = True, fix_imports = True)
p.disconnect()