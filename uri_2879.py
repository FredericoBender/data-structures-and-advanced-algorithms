n = int(input())
contaVitorias = 0

for i in range(n):
    atual=int(input())
    if(atual==2 or atual==3):
        contaVitorias+=1
        
print(contaVitorias)