n = int(input())
winsCounter = 0

for i in range(n):
    currentValue = int(input())
    if currentValue == 2 or currentValue == 3:
        winsCounter += 1
        
print(winsCounter)