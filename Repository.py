from math import sqrt

import numpy as np
import networkx as nx
from random import randint

def loadData(filename):
    net = {}
    matrix = []
    file = open(filename, "r")
    numberOfCities = int(file.readline())
    net['noCit'] = numberOfCities
    for i in range(numberOfCities):
        mat =[]
        line = file.readline()
        elem = line.split(",")
        for j in range(numberOfCities):
            mat.append(int(elem[j]))
        matrix.append(mat)
    file.close()
    net['mat'] = matrix
    return net


def loadHard(filename):
    graph = []
    net = {}
    numberOfNodes = 0
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    startIndex = 0
    for linie in lines:
        if linie.startswith("DIMENSION"):
            numberOfNodes = int(linie.split(" ")[2])
        if linie[0].isdigit():
            break
        startIndex += 1
    values = []
    net['noCit'] = numberOfNodes
    for index in range(0, numberOfNodes):
        i = startIndex+index
        x = float(lines[i].split(" ")[1])
        y = float(lines[i].split(" ")[2])
        values.append([x, y])
    for i in values:
        linie = []
        for j in values:
            x = abs(i[0] - j[0])
            y = abs(i[1] - j[1])
            rez = sqrt((x * x) + (y * y))
            linie.append(rez)
        graph.append(linie)
    net['mat'] = graph
    return net



