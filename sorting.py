#encoding=utf-8
import random

def InsertionSort(valuesList):
	"""O(n²) -> Return valuesList"""
	n = len(valuesList)
	for i in range(1,n):
		for j in range(i,0,-1):
			if (valuesList[j-1]>valuesList[j]):
				valuesList[j-1], valuesList[j] = valuesList[j], valuesList[j-1]
	return valuesList

def SelectionSort(valuesList):
	"""O(n²) -> Return valuesList"""
	n = len(valuesList)
	for j in range(n):
		indexLowestValue = j
		for i in range(j, n):
			if (valuesList[i]<valuesList[indexLowestValue]):
				indexLowestValue=i
		valuesList[j], valuesList[indexLowestValue] = valuesList[indexLowestValue], valuesList[j]
	return valuesList

def BubbleSort(valuesList):
	"""O(n²) -> Return valuesList"""
	n = len(valuesList)
	for j in range(n-1):
		for i in range(n-1):
			if (valuesList[i]>valuesList[i+1]):
				valuesList[i], valuesList[i+1] = valuesList[i+1], valuesList[i]
	return valuesList


def MergeSort(valuesList, start=0, end=None): 
	"""O(n log n) -> Return valuesList"""
	def Merge(valuesList, start, middle, end):
		left = valuesList[start:middle]
		right = valuesList[middle:end]
		topLeft , topRight = 0 , 0
		for i in range(start,end):
			if (topLeft >= len(left)):
				valuesList[i]=right[topRight]
				topRight+=1
			elif (topRight >= len(right)):
				valuesList[i]=left[topLeft]
				topLeft+=1
			elif (left[topLeft] < right[topRight]):
				valuesList[i]=left[topLeft]
				topLeft+=1
			else:
				valuesList[i]=right[topRight]
				topRight+=1

	if (end==None):
		end=len(valuesList)

	if (end-start>1):
		middle = (end + start)//2
		MergeSort(valuesList, start, middle)
		MergeSort(valuesList, middle, end)
		Merge(valuesList, start, middle, end)
	return valuesList

def QuickSort(valuesList,start=0,end=None): 
	"""O(n log n) -> Return valuesList"""	
	def Partition(valuesList, start, end):
		pivot = valuesList[end]
		i = start
		for j in range(start, end):
			if (valuesList[j]<= pivot):
				valuesList[i], valuesList[j] = valuesList[j], valuesList[i]
				i+=1
		valuesList[i], valuesList[end] = valuesList[end], valuesList[i]
		return i

	if (end==None):
		end = len(valuesList)-1

	if (start < end):
		pivot = Partition(valuesList, start, end)
		QuickSort(valuesList, start, pivot-1)
		QuickSort(valuesList, pivot+1, end)
	return valuesList


def CountingSort(valuesList): 
	"""O(n) -> Return valuesList"""
	n = len(valuesList)
	biggestValue=valuesList[0]
	for i in valuesList[1:n:1]: #Take the biggestValue 
		if (i>biggestValue):
			biggestValue=i
	counters = [0] * (biggestValue+1) 
	for i in valuesList[0:n:1]: #Count the elements
		counters[i]+=1
	del valuesList[:]
	for i in range(len(counters)): 
		for j in range(counters[i]):
			valuesList.append(i) 
	return valuesList

######## How to choose? ########
#1 - InsertionSort -> n<2000
	#2 - CountingSort -> n + largest element value < 2.000.000, integers
		#3 - QuickSort -> n<100.000
#range 4 = (1,2,3]

n = 3000
valuesList = list(range(n))
random.shuffle(valuesList)
#print(valuesList)

#valuesList = InsertionSort(valuesList)
#valuesList = SelectionSort(valuesList)
#valuesList = BubbleSort(valuesList)
#valuesList = MergeSort(valuesList)
valuesList = QuickSort(valuesList)
#valuesList = CountingSort(valuesList)

#print("\n"+str(valuesList))