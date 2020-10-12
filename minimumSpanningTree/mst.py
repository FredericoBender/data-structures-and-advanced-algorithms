def Euclidean_Distance(x0,y0,x1,y1):
    return (((x0 - x1)**2) + ((y0 - y1)**2))**0.5

def getDataFrom(arq):
    values = list(csv.reader(open(arq), delimiter=","))
    del values[0]
    values = np.array(values).astype("float")
    return values

def getEdgesFrom(values):
    edges = []
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            edges.append([i, j, Euclidean_Distance(values[i][0], values[i][1], values[j][0], values[j][1])])
    return edges

import csv
import numpy as np

nodes = getDataFrom("flame.csv")
edges = getEdgesFrom(nodes)
edges.sort(key = lambda x: x[2]) #Ordena pelo 2 elemento

currentTrees = [{edges[0][0], edges[0][1]}] #Conjunto de sub arvores atuais
minimumSpanningTree=[[edges[0][0], edges[0][1]]] #Resultado

for i in edges: #i=[no1,no2,distancia]
    newTree = True
    counter = 0
    indices = []
    for index, j in enumerate(currentTrees): #j=set(elements used)
        if (i[0] in j) and (i[1] in j): #Ambos nós já em sub arvore, só ignora o caso
            newTree = False
            break
        if (i[0] in j) or (i[1] in j): 
            newTree = False
            indices.append(index)
            counter += 1
            if counter == 2: #Nós em sub arvores diferentes
                minimumSpanningTree.append([i[0],i[1]])
                currentTrees[indices[0]].update(currentTrees[indices[1]])
                currentTrees.pop(indices[1])
                break
        if (index == len(currentTrees) - 1) and (counter == 1): #Quando vazio ou 1 nó existente
            newTree = False
            currentTrees[indices[0]].add(i[0])
            currentTrees[indices[0]].add(i[1])
            minimumSpanningTree.append([i[0], i[1]])
    if newTree:
        currentTrees.append(set())
        currentTrees[-1].add(i[0])
        currentTrees[-1].add(i[1])
        minimumSpanningTree.append([i[0], i[1]])

# GRAPHIC GENERATOR #####################################################################################################

#Example: https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/nan_test.html#sphx-glr-gallery-lines-bars-and-markers-nan-test-py
from matplotlib import pyplot as plt 
import pandas as pd

def Connect(x, y, connectionType="intraClass"):
    colorSelected = "silver"
    if connectionType == "interClass":
        colorSelected = "black"
    plt.plot(x, y, color=colorSelected)

datasets = ["flame"]
rows, columns = 1, 1
plt.figure(figsize=(15, 15))

for row in range(rows):
    for col in range(columns):
        if row*rows + col >= len(datasets):
            break
        data = pd.read_csv(datasets[row*rows + col] + ".csv") 
        plt.subplot(columns, rows, row*rows + col + 1)
        plt.axis("equal")
        for i in minimumSpanningTree:
            typeLigation = "intraClass"
            if nodes[i[0]][2] != nodes[i[1]][2]:
                typeLigation = "interClass"
            Connect([nodes[i[0]][0], nodes[i[1]][0]], [nodes[i[0]][1], nodes[i[1]][1]], typeLigation)

        for name, group in data.groupby("species"):
            plt.plot(group["x"], group["y"], marker="o", linestyle="", label=name)
        plt.grid(True)
        plt.title(datasets[row*rows + col])
        plt.legend(loc="center right", bbox_to_anchor=(1.12, 0.5))

plt.show()
#plt.savefig("datasets.svg")