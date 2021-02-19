#encoding=utf-8

def BinarySearch(valuesList, value, left=0, right=None):
    if right == None:
        right = len(valuesList) - 1
    if right >= left:
        index = left + (right - left)//2
        if valuesList[index] == value:
            return [value, index]
        if valuesList[index] > value:
            return BinarySearch(valuesList, value, left, index - 1)
        else:
            return BinarySearch(valuesList, value, index + 1, right)
    return [None, None]

if __name__ == "__main__":
    valuesListSyze = 1000
    valuesList = list(range(valuesListSyze))
    value = int(input("Choose a value to search: "))
    print("Value: " + str(BinarySearch(valuesList, value)[0]))
    print("Index: " + str(BinarySearch(valuesList, value)[1]))