import random
from os import walk
import matplotlib.pyplot as plt

filenames = next(walk("datasets/"), (None, None, []))[2]
maxClusterNumber = 999999

def getPointsData(filename):
    pointsArray = []
    with open(f'datasets/{filename}', "r") as f:
        line = f.readline()
        while line:
            currentPoint = line.strip().split()
            currentPoint = [int(currentPoint[0]), int(currentPoint[1])]
            pointsArray.append(currentPoint)
            line = f.readline()

    return pointsArray


def clusterization(array, clustersNumber):
    n = len(array)  # number of rows
    dim = len(array[0])  # number of dimensions

    cluster = [[0 for i in range(dim)] for q in range(clustersNumber)]
    clusterContent = [[] for i in range(clustersNumber)]

    for i in range(dim):
        for q in range(clustersNumber):
            cluster[q][i] = random.randint(1, maxClusterNumber)

    clusterContent = dataDistribution(array, cluster)

    previousCluster = cluster
    while 1:
        cluster = updateCluster(cluster, clusterContent, dim)
        clusterContent = dataDistribution(array, cluster)
        if cluster == previousCluster:
            break

    return clusterContent


def dataDistribution(array, cluster):
    n = len(array)
    dim = len(array[0])
    clusterContent = [[] for i in range(clustersNumber)]

    for i in range(n):
        minDistance = 999999
        suitableCluster = -1
        for j in range(clustersNumber):

            distance = 0
            for q in range(dim):
                distance += (int(array[i][q]) - int(cluster[j][q])) ** 2

            distance = distance ** (1 / 2)
            if distance < minDistance:
                minDistance = distance
                suitableCluster = j

        clusterContent[suitableCluster].append(array[i])

    return clusterContent


def updateCluster(cluster, clusterContent, dim):
    k = len(cluster)

    for i in range(k):
        for q in range(dim):
            updatedParameter = 0
            for j in range(len(clusterContent[i])):
                updatedParameter += clusterContent[i][j][q]

            if len(clusterContent[i]) != 0:
                updatedParameter = updatedParameter / len(clusterContent[i])
            cluster[i][q] = updatedParameter
    return cluster


def visualizeCluster(clusterContent):
    k = len(clusterContent)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")

    for i in range(k):
        xCoords = []
        yCoords = []
        for q in range(len(clusterContent[i])):
            xCoords.append(clusterContent[i][q][0])
            yCoords.append(clusterContent[i][q][1])
        plt.scatter(xCoords, yCoords)

    print('Showing clusters scatter...')
    plt.show()


def visualizePoints(points):
    plt.scatter(*zip(*points))
    print('Showing initial points scatter...')
    plt.show()


while True:
    try:
        for i in range(len(filenames)):
            print(f'{i + 1}. {filenames[i]}')
        choice = int(input("Choose dataset number: "))
    except ValueError:
        print("Invalid input, try again\n")
        continue
    else:
        if choice < 1 or choice > len(filenames):
            print("Invalid input, try again\n")
            continue
        print("File successfully opened...")
        break

while True:
    try:
        clustersNumber = int(input("Enter number of clusters: "))
    except ValueError:
        print("Invalid input, try again\n")
        continue
    else:
        if clustersNumber < 1 or clustersNumber > maxClusterNumber:
            print("Invalid input, try again\n")
            continue
        break



pData = getPointsData(filenames[choice - 1])
visualizePoints(pData)
visualizeCluster(clusterization(pData, clustersNumber))
print("End")