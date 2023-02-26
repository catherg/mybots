import constants as c
import matplotlib

x_arr = []
for i in range(0,5):
    x_arr = i

y_arr = c.fitness_arr
print("y_arr")

matplotlib.plot(x_arr, y_arr, label = "line 1")