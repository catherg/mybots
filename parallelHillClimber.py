from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}

        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
    
    def Evolve(self):
        for i in range(0, c.populationSize):
            self.parents[i].Start_Simulation("GUI")

        for i in range(0, c.populationSize):
            self.parents[i].Wait_For_Simulation_To_End()

        #for currentGeneration in range(c.numberofGenerations):
        #    self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")

        self.Print()

        self.Select()

    def Spawn(self):
        self.childs = {}
        for i in range(0, c.populationSize):
            self.childs[i] = copy.deepcopy(self.parents[i])
            self.childs[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        #self.childs.Mutate()
        pass

    def Select(self):
        #if self.parent.fitness < self.child.fitness:
         #   self.parent = self.child
         pass

    def Print(self):
        print("parent:", self.parent.fitness, "child:", self.child.fitness)

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass
