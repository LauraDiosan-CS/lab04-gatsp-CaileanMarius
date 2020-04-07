from random import randint, seed


#
# def generateARandomPermutation(n):
#     perm = [i for i in range(n)]
#     pos1 = randint(0, n - 1)
#     pos2 = randint(0, n - 1)
#     perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
#     return perm


# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        # self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
        # self.__repres = [i for i in range(self.__problPama['noNdes'])]

        self.__repres = self.getRepres()
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def getRepres(self):
        representation = [1 for _ in range(0, self.__problParam['noNodes'])]
        for i in range(1, self.__problParam['noNodes']):
            number = 0
            number = randint(2, self.__problParam['noNodes'])
            if number not in representation:
                representation[i] = number
            elif number in representation:
                while number in representation:
                    number = randint(2, self.__problParam['noNodes'])
                representation[i] = number
        return representation

    def crossover(self, c):
        #order XO
        pos1 = randint(1, self.__problParam['noNodes'] - 1)
        pos2 = randint(1, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2+1]
        for el in c.__repres[pos2+1:] + c.__repres[1:pos2+1]:
            if el not in newrepres:
                if len(newrepres) < self.__problParam['noNodes'] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1
        new = [1]+newrepres

        offspring = Chromosome(self.__problParam)
        offspring.repres = new
        return offspring


    def mutation(self):

        pos1 = randint(1, len(self.__repres) - 1)
        pos2 = randint(1, len(self.__repres) - 1)

        self.repres[pos1], self.repres[pos2] = self.repres[pos2], self.repres[pos1]

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
