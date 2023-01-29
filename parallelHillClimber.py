from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #for i in range(0, c.populationSize):
        #    for j in range(0, c.numberofGenerations):
        #        os.system("rm brain" + str(i * j) + ".nndf")
        #        os.system("rm fitness" + str(i * j) + ".txt")
        self.nextAvailableID = 0
        self.parents = {}

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

    def Select(self):
        for i in range(0, c.populationSize):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        for i in range(0, c.populationSize):
            print("\n parent:", self.parents[i].fitness, "child:", self.children[i].fitness, "\n")

    def Show_Best(self):
        lowest = 0
        for i in range(0, c.populationSize):
            if self.parents[i].fitness < self.parents[lowest].fitness:
                lowest = i
        self.parents[lowest].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(0, c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(0, c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

