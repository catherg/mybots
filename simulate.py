#import random
#import pyrosim.pyrosim as pyrosim
#import pybullet as p
#import pybullet_data
#import time
#import numpy
#import math
import constants as c
from simulation import SIMULATION
import sys
#from robot import ROBOT

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness(solutionID)

##amplitude = numpy.pi / 4
##frequency = 0.04
##phaseOffset = 50

##back_amplitude = numpy.pi / 4 + 20
##back_frequency = 5
##back_phaseOffset = numpy.pi / 4 + 50

##front_amplitude = numpy.pi / 4 - 20
##front_frequency = 5
##front_phaseOffset = 0 - 50

#//physicsClient = p.connect(p.GUI)
#//p.setAdditionalSearchPath(pybullet_data.getDataPath())
##sleep = 1/60
#//p.setGravity(0,0,-9.8)
#--planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#--p.loadSDF("world.sdf")
#//pyrosim.Prepare_To_Simulate(robotId)
#backLegSensorValues = numpy.zeros(1000)
#frontLegSensorValues = numpy.zeros(1000)
##targetAngles = numpy.sin(numpy.linspace(0, numpy.pi * 2, num=1000)) * (numpy.pi / 4)
#targetAngles = c.amplitude * numpy.sin(c.frequency * numpy.linspace(0, 1000, num=1000) + c.phaseOffset)
#back_targetAngles = c.back_amplitude * numpy.sin(c.back_frequency * numpy.linspace(0, 1000, num=1000) + c.back_phaseOffset)
#front_targetAngles = c.front_amplitude * numpy.sin(c.front_frequency * numpy.linspace(0, 1000, num=1000) + c.front_phaseOffset)
##numpy.save('data/targetAngle.npy', targetAngles, allow_pickle = True, fix_imports = True)
##exit()
#for i in range(0, 1000):
  #  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
 #   frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
  #  pyrosim.Set_Motor_For_Joint(
  #  bodyIndex = robotId,

   # jointName = b'Torso_Backleg',

   # controlMode = p.POSITION_CONTROL,

    ##targetPosition = random.random() * 0.5 - 0.25,
   # targetPosition = back_targetAngles[i],

  #  maxForce = c.maxForce)

  #  pyrosim.Set_Motor_For_Joint(
  #  bodyIndex = robotId,

  #  jointName = b'Torso_Frontleg',

 #   controlMode = p.POSITION_CONTROL,

    ##targetPosition = random.random() * 0.5 - 0.25,
 #   targetPosition = front_targetAngles[i],

  #  maxForce = c.maxForce)

 #   p.stepSimulation()
  #  time.sleep(c.sleep)
#targetAngles = numpy.sin(numpy.linspace(-2, 2, 201))
#numpy.save('data/backLegSensor.npy', backLegSensorValues, allow_pickle = True, fix_imports = True)
#numpy.save('data/frontLegSensor.npy', frontLegSensorValues, allow_pickle = True, fix_imports = True)
#numpy.save('data/targetAngle.npy', targetAngles, allow_pickle = True, fix_imports = True)
#p.disconnect()