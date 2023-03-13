import os
import numpy
from hillclimber import HILLCLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER
phc = PARALLEL_HILL_CLIMBER()
numpy.random.seed(3)
phc.Evolve()
print("GENERATIONS ALL DONE!")
input("Press Enter to Continue")
phc.Show_Best()