import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)
sleep = 1/60
p.loadSDF("box.sdf")
for i in range(0, 1000):
    p.stepSimulation()
    time.sleep(sleep)
    print(i)
p.disconnect()