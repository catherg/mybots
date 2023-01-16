import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load('data/backLegSensor.npy', allow_pickle = True)
frontLegSensorValues = numpy.load('data/frontLegSensor.npy', allow_pickle = True)
targetAngles = numpy.load('data/targetAngle.npy', allow_pickle = True)
#matplotlib.pyplot.plot(backLegSensorValues, label = "back leg", linewidth = '5')
#matplotlib.pyplot.plot(frontLegSensorValues, label = "front leg")
#matplotlib.pyplot.legend()
matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.show()