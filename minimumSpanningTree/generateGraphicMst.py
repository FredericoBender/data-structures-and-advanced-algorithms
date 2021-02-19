#Example: https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/nan_test.html#sphx-glr-gallery-lines-bars-and-markers-nan-test-py
from mst import *
from matplotlib import pyplot as plt 
import pandas as pd

def Connect(x, y, connectionType="intraClass"):
    colorSelected = "silver"
    if connectionType == "interClass":
        colorSelected = "black"
    plt.plot(x, y, color=colorSelected)



datasets = ["aggregation","compound","pathbased","spiral","D31","R15","jain","flame"]
rows, columns = 8, 1

plt.figure(figsize=(columns*11, rows*11))
for row in range(rows): #[0,1]
    for col in range(columns):#[0,1,2]
        if row*columns + col >= len(datasets):
            break
        nodes = getDataFrom("data/" + datasets[row*columns + col] + ".csv")
        edges = getEdgesFrom(nodes)
        minimumSpanningTree = kruskal(edges)

        data = pd.read_csv("data/" + datasets[row*columns + col] + ".csv") 
        plt.subplot(rows, columns, row*columns + col + 1)
        plt.axis("equal")
        for i in minimumSpanningTree:
            typeLigation = "intraClass"
            if nodes[i[0]][2] != nodes[i[1]][2]:
                typeLigation = "interClass"
            Connect([nodes[i[0]][0], nodes[i[1]][0]], [nodes[i[0]][1], nodes[i[1]][1]], typeLigation)

        for name, group in data.groupby("species"):
            plt.plot(group["x"], group["y"], marker="o", linestyle="", label=name, ms=2) #ms = marker size
        plt.grid(True)
        plt.title(datasets[row*columns + col])
        plt.legend(loc="center right", bbox_to_anchor=(1.12, 0.5))

#plt.show()
plt.savefig("mst.svg")