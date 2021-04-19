### Custom Classification ####################################################
from sklearn import tree

#caracteristicas do carro = cavalos de potencia, numero de assentos
features = [[300, 2],[450, 2],[200, 8 ],[150 , 9]]
labels = ["sport_car","sport_car","minivan","minivan"] #classes
clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)

#preve a classe baseado nas caracteristicas
print(clf.predict([[350,2], [100, 7]]))



### Classification for IRIS ####################################################

from sklearn import tree
from sklearn import datasets

iris = datasets.load_iris()
features = iris.data
labels = iris.target

clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)

print(clf.predict([[5.1, 3.5, 1.4, 2.0]]))
