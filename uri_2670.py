a1 = int(input())
a2 = int(input())
a3 = int(input())

menor=(a2*2)+(a3*4) #1 andar
if((a1*2)+(a3*2)<menor):
    menor = (a1*2)+(a3*2) #2 andar
if((a1*4)+(a2*2)<menor):
    menor = (a1*4)+(a2*2) #3 andar

print(menor)