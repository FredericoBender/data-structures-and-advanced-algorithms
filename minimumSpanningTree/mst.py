def Euclidean_Distance(x0,y0,x1,y1):
    return (((x0-x1)**2)+((y0-y1)**2))**0.5

def Connect(point0,point1,connectionType="intraClass"):
    colorSelected="silver"
    if (connectionType=="interClass"):
        colorSelected="black"
    plt.plot(point0,point1,color=colorSelected)



import csv
import numpy as np

values = list(csv.reader(open("flame.csv"), delimiter=","))
del values[0]
values = np.array(values).astype("float")




#Example: https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/nan_test.html#sphx-glr-gallery-lines-bars-and-markers-nan-test-py
from matplotlib import pyplot as plt 
import pandas as pd

datasets=["flame"]
rows , columns = 1 , 1
plt.figure(figsize=(15,15))

for row in range(rows):
    for col in range(columns):
        if(row*rows+col>=len(datasets)):
            break
        data = pd.read_csv(datasets[row*rows+col]+".csv") 
        plt.subplot(columns, rows, row*rows+col+1)

        #Linhas de exemplo (APENAS PARA TESTE)
        Connect([1.35,1.85],[26.65,27.8])
        Connect([1.35,1.4],[26.65,23.25],"interClass")
        Connect([1.4,1.35],[23.25,22.65])
        Connect([1.1,1.35],[22.05,22.65])

        for name, group in data.groupby("species"):
            plt.plot(group["x"], group["y"], marker="o", linestyle="", label=name)
        plt.grid(True)
        plt.title(datasets[row*rows+col])
        plt.legend(loc="center right",bbox_to_anchor=(1.12, 0.5))

plt.show()
#plt.savefig("datasets.svg")