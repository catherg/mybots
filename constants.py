import numpy
import math

amplitude = numpy.pi / 4
frequency = 0.04
phaseOffset = 50

back_amplitude = numpy.pi / 4 + 20
back_frequency = 5
back_phaseOffset = numpy.pi / 4 + 50

front_amplitude = numpy.pi / 4 - 20
front_frequency = 5
front_phaseOffset = 0 - 50

sleep = 1/20

maxForce = 500

numberofGenerations = 1

populationSize = 1


numLinks = numpy.random.randint(3, 10)


numMotorNeurons = 7


motorJointRange = 0.2

x = 0.2