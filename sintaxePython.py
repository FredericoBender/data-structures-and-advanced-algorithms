# IMPORTAÇÕES  ###############################################################################

#encoding=utf-8 Evita dor de cabeça com acentos e outros caracteres
import nomeDaBiblioteca
import nomeDaBiblioteca as n #Para usar como n.função
from graphics import * #Importa tudo da biblioteca sem precisar utilizar o prefixo "graphics"

# LOOPS  #####################################################################################

while (condição):

for (i in range(5)): #(0,1,2,3,4) -> (]

# CONDIÇÕES  #################################################################################

if(condição):

else:

# ENTRADA e PRINT  ###########################################################################

x = int(input("digite o que você quer ler"))

print("oi %s %d %f" % ("fredi",1,1.0)) #Interpolação de Strings mais eficiente
print("{} é um número melhor que {}".format(var1, var2))
print(str(x) + "seu valor")

# FUNÇÕES  ###################################################################################

def nomeDaFuncao(parametro1, parametro2):    ...
    return variavelRetornada

def fatorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fatorial(n-1)

# TIPOS DE DADO  ############################################################################# 

X = int(3)
X = float(3.1415)
X = str(2) #Converte em string
X = u"batata" #String Unicode em python, agora pode utilizar qualquer caractere do mundo
X = "batata"
X = True 
X = False

# LISTAS e SEUS MÉTODOS#######################################################################

lista = []
lista.append(4) #Adiciona o valor 4
lista.pop(índice) #Remove o valor desse índice
lista.remove(valor) #Remove o 1º caso desse valor
len(lista) #Retorna o tamanho da lista

lista = [0] * 10 #Cria lista de tamanho 10 zerada
del lista[:] #Apaga elementos de uma lista sem exclui-lá
print(string[0:3]) #Vai printar parte da string "bat" (0,1,2)
linha.strip() #Remove caracteres especiais no fim da linha
" ".join(lista) #Pega uma lista de strings e concatena em uma string que separa os itens por " "
x = input().split(" ") #Le varios valores na mesma linha do terminal

# DICIONÁRIOS e SEUS MÉTODOS  ################################################################

dicionário = #Cada chave tem um valor, pode ser uma lista {"A":"Alouuu","B":"Batata","C":"Cabeça"} #Dicionário composto por chave e itens
print(dicionário["A"]) #Mostra os elementos daquela chave
dicionário["D"]="Dado" #Adiciona o elemento ao dicionário
dicionário.get("Chave", "Mensagem caso não encontre") #Para buscar um valor pela chave
dicionário.pop("Chave", "Mensagem caso não encontre") #Para apagar um valor

dicionário.keys()
dicionário.values()

dicionário.update(dic2) #Mescla 2 dicionários

# ARQUIVOS  ##################################################################################

arq = open("arquivo.nome","w") #Escreve
arq = open("arquivo.nome","r") #Le
arq = open("arquivo.nome","a") #Escreve no final
arq.close() #Sempre usar no final
arq.write("sequência") #Escreve no arquivo

# COMENTÁRIOS  ###############################################################################

#Se utiliza Hashtag, ou ''' '''
''' bloco de comentário'''

# ORIENTAÇÃO A OBJETOS #######################################################################

def __init__(self) -> é o construtor que executa sempre que instanciar a classe
def _privado(self) -> 1 _ significa atributo privado
def__getitem__(self) -> estamos usando sobrecarga de operadores, para escrever na forma nativa da linguagem, utilizando os operadores da linguagem sobre o objeto
def __repr__(self) -> usado para mostrar o objeto ao programador
def __str__(self) -> usado para mostrar o objeto ao usuário final
#Python não tem sobrecarga de funções(quando existe a mesma função com número diferente de parâmetros)

self -> é utilizado para referenciar atributos do próprio objeto
ex:(diferença de altura entre 2 objetos) - > return self.altura - outro.altura

# EXTRAS  ####################################################################################

if (__name__=="__main__"): -> Não executa o if se o código for importado

try:  #Tenta fazer isso
except: #Se der erro, "Except", faz isso
    
break, continue, e pass #Quebra loop, volta pro início do loop, e continua logo na linha abaixo

def fx(function,x): #Passando literalmente a função desejada para fx
    fx=eval(function)
    return fx
print(fx("x*3",2))

string.find("ta") #Retorna posição desse elemento #Retorna -1 se não encontrar o elemento
string.replace("string","novastring") #Substitui

#Expressões regulares ########################################################################

#import re
^ $ #Procura no Início ou Fim POUCO USADO, É MAIS PRA VALIDAR
. #Pega todos os caracteres (menos \n)

[] #São alternativas]
[^abc] #Qualquer caractere menos "a" "b" ou "c'
[.] = \. #Literalmente busca o ponto #sintaxe equivalente

* + ? #Procura por: 0 ou mais, 1 ou mais , 0 ou 1
{2,5} #Procura por 2 a 5 ocorrências

| #Ou
() #Grupo de busca, vai buscando por ordem dos parenteses, cada grupo é inserido em uma lista
(?:) #Usado para não capturar esse grupo

\d \D #Números, NÃO números
\s \S #Espaços, NÃO espaços
\w \W #Números e letras, NÃO números e letras

print re.search("padrão ou RE","Vai buscar se o padrão está contido nesta string") #Busca uma ocorrência
#PS: Para extrair o objeto usar:
var.group()

print re.findall("padrão ou RE","Vai buscar se o padrão está contido nesta string") #Busca todas as ocorrências

ex:
import re
string = "bjdgs  s laplace@gmail.com.br aasfk jjk akkka kj thales@naosei.br h pradomatheus@yahoo.br baide"
lista = re.findall("([\w._-]*@[a-z]*\.(?:com\.br|com|br))",string)
print(lista)