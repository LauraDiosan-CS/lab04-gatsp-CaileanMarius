from random import randint

from Chromosome import *


class GA:
    def __init__(self, problParams=None, gaParams=None):
        #self.__mat = mat
        self.__problParams = problParams
        self.__gaParams = gaParams
        self.__population = []



    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__gaParams['popSize']):
            c = Chromosome(self.__problParams)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParams['function'](c.repres, self.__problParams["mat"])

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__gaParams['popSize'] - 1)
        pos2 = randint(0, self.__gaParams['popSize'] - 1)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__gaParams['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__gaParams['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__gaParams['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParams['function'](off.repres, self.__problParams['mat'])
            worst = self.worstChromosome()
            if off.fitness < worst.fitness:
                for i in range(self.__gaParams['popSize']):
                    if self.__population[i] == worst:
                        self.__population[i] = off
                        break