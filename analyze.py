import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load(data/backLegSensorValues.npy)
print(backLegSensorValues)
plot(backLegSensorValues)
matplotlib.pyplot.show()
