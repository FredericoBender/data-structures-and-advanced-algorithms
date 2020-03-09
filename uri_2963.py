n = int(input())
candidatos = []
aprovado = True

for i in range(n):  
    atual = int(input())
    candidatos.append(atual)
    if(i>0) and (atual>candidatos[0]):
        aprovado=False
        
if(aprovado):
    print("S")
else:
    print("N")