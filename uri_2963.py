n = int(input())
candidatesList = []
approved = True

for i in range(n):  
    currentValue = int(input())
    candidatesList.append(currentValue)
    if i > 0 and currentValue > candidatesList[0]:
        approved = False
        
if approved:
    print("S")
else:
    print("N")