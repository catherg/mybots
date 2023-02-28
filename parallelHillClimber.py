from solution import SOLUTION
import constants as c
import copy
import os
import matplotlib.pyplot as plt

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        #self.fitness_arr = []

        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
    
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberofGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)

        self.Print()

        self.Select()


    def Spawn(self):
        self.children = {}
        for i in range(0, c.populationSize):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
            

    def Mutate(self):
        for i in range(0, c.populationSize):
            self.children[i].Mutate()
            self.children[i].Mutate_Body()

    def Select(self):
        for i in range(0, c.populationSize):
            if self.parents[i].fitness < self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        for i in range(0, c.populationSize):
            print("\n parent:", self.parents[i].fitness, "child:", self.children[i].fitness, "\n")

    def Show_Best(self):
        highest = 0
        for i in range(0, c.populationSize):
            if self.parents[i].fitness > self.parents[highest].fitness:
                highest = i
        print("HIGHEST:", self.parents[highest].fitness)
        self.parents[highest].Start_Simulation("GUI")
        print("FITNESS ARRAY:", c.fitness_arr)
        x_arr = []
        for i in range(0,101):
            x_arr.append(i)

        plt.plot(x_arr, c.fitness_arr)
        plt.show()

    def Evaluate(self, solutions):
       
        for i in range(0, c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
           

        highest = -50
        for i in range(0, c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()
            if self.parents[i].fitness > highest:
                highest = self.parents[i].fitness
        c.fitness_arr.append(highest)

    
