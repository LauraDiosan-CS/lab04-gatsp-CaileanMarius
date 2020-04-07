

def getDistance(c, mat):
    totalCost = 0;
    for i in range(0, len(mat) - 1):
        # print(matrix[c.repres[i]][c.repres[i+1]])
        totalCost += mat[c[i] - 1][c[i + 1] - 1]
    totalCost += mat[c[-1] - 1][c[0] - 1]
    return totalCost