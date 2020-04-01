n = int(input())
k = int(input())
orderedList = [0] * 1001
currentIndex = 1000
approvedCounter = 0

for i in range(n):
    currentValue = int(input())
    orderedList[currentValue]+=1

while(currentIndex>=0):
    approvedCounter+=orderedList[currentIndex]
    if (approvedCounter>= k):
        break
    currentIndex-=1

print(approvedCounter)