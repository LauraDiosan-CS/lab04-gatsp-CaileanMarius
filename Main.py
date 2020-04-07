from random import randint
import Repository
import Chromosome
from GA import *
from Utils import *


def main():
    net = {}
    net = Repository.loadHard("hardE.txt")
    #net = Repository.loadData("mediumF.txt")
    # print(net['mat'])
    dim = net['noCit']
    # print(dim)
    matrix = net['mat']


    # totalCost =0;
    # cr=[1,2,4,3]
    # mat = [[0, 6, 12, 10], [6, 0, 8, 4], [12, 8, 0, 15], [10, 4, 15, 0]]
    # for i in range(0, len(mat)-1):
    #     # print(matrix[c.repres[i]][c.repres[i+1]])
    #     totalCost += matrix[cr[i] - 1][cr[i+1] - 1]
    # totalCost += matrix[cr[-1] - 1][cr[0] - 1]
    # print(totalCost)


    problParams = {'noNodes': dim, 'mat': matrix, 'function':getDistance}
    gaParams = {'popSize': 100, 'noGen': 250}


    # representation = [1 for _ in range(0, dim*dim)]
    # for i in range(1, dim*dim):
    #     number = 0
    #     number = randint(2, dim*dim)
    #     if number not in representation:
    #         representation[i] = number
    #     elif number in representation:
    #         while number in representation:
    #             number = randint(2,dim*dim)
    #         representation[i] = number
    # print(representation)

    ga = GA(problParams, gaParams)
    ga.initialisation()
    ga.evaluation()


    for generation in range(gaParams['noGen']):
        #ga.oneGenerationElitism()
        ga.oneGenerationSteadyState()
        bestChromo = ga.bestChromosome()
        print('Cel mai bun crom din generatia ' + str(generation + 1) + ' : x = ' + str(
            bestChromo.repres) + ' cu distanta = ' + str(bestChromo.fitness))
        print("--------------------------------------------------------------------------------------")


    bestChromo = ga.bestChromosome()
    print("\n\n")
    print('Cel mai bun crom  : x = ' + str(
        bestChromo.repres) + ' cu distanta = ' + str(bestChromo.fitness))




main()