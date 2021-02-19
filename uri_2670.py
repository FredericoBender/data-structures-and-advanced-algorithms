firstFloor = int(input())
secondFloor = int(input())
thirdFloor = int(input())

lowestValue = (secondFloor*2) + (thirdFloor*4) #first floor
if (firstFloor*2) + (thirdFloor*2) < lowestValue:
    lowestValue = (firstFloor*2) + (thirdFloor*2) #second floor
if (firstFloor*4) + (secondFloor*2) < lowestValue:
    lowestValue = (firstFloor*4) + (secondFloor*2) #third floor

print(lowestValue)