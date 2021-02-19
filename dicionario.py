print(help(list)) #Ajuda na hora de programar Sobrecarga de operadores

# PONTEIROS  ###########################################################################################

    #LISTAS, DIC, e SETS  quando passados por parâmetro mandam um endereço, assim como todas variáveis, porém se for copiar essa estruturas, deve ser utilizado uma função para tal.
    from copy import deepcopy
    x=[["a","b",[1,2,3]],[1,2]]
    y = x.copy() #Só vai copiar a (lista ou dic ou set) mais externa
    y = deepcopy(x) #Vai copiar todas as (listas, dics e sets) aninhadas

#IMPORTAÇÕES, pode importa funções, classes, e variáveis ###############################################################################

    #encoding=utf-8 Evita dor de cabeça com acentos e outros caracteres
    import nomeDaBiblioteca
    import nomeDaBiblioteca as n #Para usar como n.função
    from graphics import * #Importa tudo da biblioteca sem precisar utilizar o prefixo "graphics"
    from nomeDaBiblioteca import variavelN #Importa tudo da biblioteca sem precisar utilizar o prefixo "graphics"
    x = nomeDaBiblioteca.nomeDaVariável #Importa o valor de uma variável
    
# LOOPS  #####################################################################################

    while (condição): #Utilizado quando não sabemos quantas iterações vão ocorrer!

    for i, elem in enumerate(lista): #enumerate retorna lista de tuplas
    
    for (i in range(5)): #(0,1,2,3,4) -> (]

# CONDIÇÕES  #################################################################################

    if(condição): print("oi") #Se o bloco tiver apenas uma linha, pode ser escrito na mesma
    else:
    x = valor 1 if condição else valor 2

# ENTRADA e PRINT  ###########################################################################

    x = int(input("digite o que você quer ler"))

    print("oi %s %d %f" % ("fredi",1,1.0)) #Interpolação de Strings mais eficiente
    print("{1:.2f} é um número {0} melhor que {1}".format(var1, var2))
    print(str(x) + "seu valor")

# FUNÇÕES  ###################################################################################

    def nomeDaFuncao(parametro1, parametro2 = 2): #O parâmetro 2 é opcional
        """Descrição do que faz"""
        global x #Se modificar a variável "x", vai mudar ela no escopo global
        variavelRetornada = 2
        return variavelRetornada

    def fatorial(n):
        global x #Diz que essa variável, vai mudar a variável Global!
        if(n==0 or n==1):
            return 1
        else:
            return n * fatorial(n-1)
    
    def teste(*lista,**dicionario): #Usado quando não sabemos quantos argumentos vai ter, "lista" vai ser uma lista com todos elementos, e "dicionario" um dicionario

    def funcao(x,y,z): 
    lista = [1,2,3]
    funcao(*lista) #Desmembrando lista para passagem de parâmetro
    
    def fx(function,x): #Passando literalmente a função desejada para fx
        fx=eval(function)
        return fx
    print(fx("x*3",2))
    
    amp = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** .5 #Função Lambda
    print amp(1, 1, 1)
    
    def myfunc(n):
        return lambda a : a * n #Está retornando uma função anônima
    mydoubler = myfunc(2)
    print(mydoubler(11))
    
# TIPOS DE DADO  ############################################################################# 

    x, y, z = "Orange", "Banana", "Cherry"
    x = y = z = 2
    
    X = int(3)
    X = float(3.1415)
    X = complex(3 + 4j)
    X = range(0,7,2) #(0,2,4,6)
    print(X.real, X.imag, c.conjugate()) #Conjugado é o mesmo com a parte imaginária invertida
    
    X = str(2) #Converte em string (IMUTÁVEL)
    X = u"batata" #String Unicode em python, agora pode utilizar qualquer caractere do mundo
    X = "batata"
    X = bool(15) #retorna True 
    X = False
    X = (1,) #Tupla é (IMUTÁVEL)
    tuple([1,2,3]) #Converte lista em tupla
    list((1,2,3)) #Converte tupla em lista
    dict(brand="Ford", model="Mustang", year=1964) #Converte em dicionario
   
# SETS e SEUS MÉTODOS #######################################################################################
    
    s1 = set(range(3)) #MUTÁVEL, SEM REPETIÇÃO, SEM ORDEM
    s1 = {1, 5, 7} #Cria set com estes valores
    s1.add(4) #Adiciona 1 item
    s1.update([1,2,3,4]) #Adiciona dados do 2º set ao primeiro
    s1.remove(1) #Elimina o item 1
    
    s1 = frozenset(range(3)) #IMUTÁVEL, SEM REPETIÇÃO, SEM ORDEM
    
    print(s1.difference(s2), s1.intersection(s2), s1.union(s2))
    s1.issuperset(s2): #Return True if all items set 's2' are present in set 's1'
    s1.issubset(s2): #Return True if all items set 's1' are present in set 's2'
    s1.isdisjoint(s2): #Testa se NÃO tem itens em comum
    s1.symmetric_difference(s2) #União - Intesecção
    
# LISTAS e SEUS MÉTODOS#######################################################################

    lista = [0] * 10 #Cria lista de tamanho 10 zerada
    
    lista = []
    lista.append(4) #Adiciona o valor 4
    lista.insert(1, "orange") #Insere um elemento no meio da lista, sem substituir nada
    lista.remove(valor) #Remove o 1º caso desse valor
    lista.extend(lista2) #Concatena os elementos de 2 listas
    lista.count(5) #Conta quantas vezes o elemento aparece
    lista.index(2) #Retorna o indíce do 1º elemento com esse valor
    
    lista.pop(índice) #Apaga o item nesse índice, e o retorna
    del lista[indice] #OU
    
    lista.clear() #Apaga todos os itens da lista, OU
    del lista[:]

    lista.sort() #Ordena a lista !!!GERADO SOBRE ELE MESMO!!!
    lista.reverse() #Inverte a lista !!!GERADO SOBRE ELE MESMO!!!
    
    " ".join(lista) #Retorna uma string, concatena os elementos da lista com " "
    
    all([[],(),0,"S"]) #Retorna True, se todos elementos de uma lista terem valor positivo
    any([[],(),0,"S"]) #Retorna True, se algum elemento da lista ter valor positivo
    
    x = sum([1,2,3]) #Retorna o resultado da soma de uma lista
    x = min(5, 10, 25) #Retorna o menor
    x = max(5, 10, 25) #Retorna o maior
    
# TUPLAS e SEUS MÉTODOS#######################################################################
    
    tupla.count(5) #Conta quantas vezes o elemento aparece
    tupla.index(2) #Retorna o indíce do 1º elemento com esse valor
    
# STRINGS e SEUS MÉTODOS#######################################################################
    
    string = "  oito "
    print(string[0:3]) #Vai printar parte da string "bat" (0,1,2)
    print(string[::-1]) #Vai printar a string invertida
    string.strip() #Remove espaços no início e fim, ou, o carácter passado como parâmetro
    
    string.find("ta") #Retorna posição desse elemento #Retorna -1 se não encontrar o elemento
    string.replace("string","novastring") #Substitui

    string.lower() #Deixa tudo mínusculo
    string.upper() #Deixa tudo maíusculo
    #Tem muitos outros métodos!

    x = "batata banana morango".split(" ") #Retorna uma lista, onde cada item é separado pelo parâmetro da função
    if "oi" in ["1","oi",""]: #Eficiente para buscar algo contido
        
# DICIONÁRIOS e SEUS MÉTODOS  ################################################################

    dicionário = #Cada chave tem um valor, pode ser uma lista {"A":"Alouuu","B":"Batata","C":"Cabeça"} #Dicionário composto por chave e itens
    print(dicionário["A"]) #Mostra os elementos daquela chave
    
    dicionário["D"]="Dado" #Adiciona o elemento ao dicionário
    x = dicionario.setdefault("chave", "valor") #Se essa chave não existir, insere o que foi passado de parâmetro
    
    dicionário.get("Chave", "Mensagem caso não encontre") #Para buscar um valor pela chave
    
    dicionário.clear() #Limpa o dicionario, fica vazio
    
    dicionário.pop("Chave", "Mensagem caso não encontre") #Para apagar um valor
    del dicionario["chave"]
    
    x = ('key1', 'key2', 'key3')
    dic = dict.fromkeys(x) #Cria um dicionario mais fácil, PS: pode ter um segundo parâmetro para escolher qual será o valor dos itens
    
    dicionário.keys()
    dicionário.values()
    for prog, albuns in progs.items(): #Itera sobre os ites do dicionário
        print prog, '=>', albuns

    dicionário.update(dic2) #Mescla 2 dicionários

# ARQUIVOS  ##################################################################################

    arq = open("arquivo.nome","r", encoding='utf-8') #Abre para leitura (padrão)
    arq.read() #Retorna String de tudo
    arq.readline() #Retorna String da 1ª linha
    arq.readlines() #Retorna lista com todas as linhas

    arq = open("arquivo.nome","w") #Apaga e permite escrita
    arq = open("arquivo.nome","x") #Cria o arquivo se ele não existe, retorna ERRO se existir
    arq = open("arquivo.nome","a") #Escreve no final (append)
    arq.write("sequência") #Escreve no arquivo
    arq.writelines(lista) #Escreve uma lista de strings no arquivo
    
    arq.close() #Sempre usar no final
    

    os.remove("demofile.txt") #Apaga um arquivo
    os.rmdir("myfolder") #Apaga uma pasta
    os.path.basename(): #retorna o componente final de um caminho.
    os.path.dirname(): #retorna um caminho sem o componente final.
    os.path.exists(): #retorna True se o caminho existe ou False em caso contrário.
    os.path.getsize(): #retorna o tamanho do arquivo em bytes.
    glob.glob("*.py") #retorna uma lista com os nomes de arquivo que atendem ao critério passado como parâmetro
    
# COMENTÁRIOS  ###############################################################################

    #Se utiliza Hashtag, ou ''' '''
    ''' bloco de comentário'''

# ORIENTAÇÃO A OBJETOS #######################################################################
    self # é utilizado para referenciar atributos do próprio objeto
    ex:(diferença de altura entre 2 objetos) - > return self.altura - outro.altura
    
    class Person:
        def __init__(self, name, age): # é o construtor que executa sempre que instanciar a classe
            self.name = name
            self.age = age
        def _privado(self) # um '_' significa privado
        def__getitem__(self) # dois '_' significa que estamos usando sobrecarga de operadores, para escrever na forma nativa da linguagem, utilizando os operadores da linguagem sobre o objeto
        #Python não tem sobrecarga de funções(quando existe a mesma função com número diferente de parâmetros)

        
    ## Exemplo de uso real entre REPR e STR ##
    class MyNumbers:
        def __init__(self,a,b):
            self.a = a
            self.b = b
        def __repr__(self): #Usar pra exibir ao programador, é uma linha interpretável em python, de como o computador enxerga isso
            return "MyNumbers({},{})".format(self.a,self.b)
        def __str__(self): #Usar pra exibir a informação de forma clara ao usuário
            return "{} {}".format(self.a,self.b)
    myclass = MyNumbers(3,6)
    print(repr(myclass)) 
    print(str(myclass))
    print(myclass) #print invoca função str()
        #Obs: Listas, filas, pilhas -> STR = REPR
        #     Outras estruturas que TEM como representar o objeto, CRIAR REPR
        #     Outras estruturas que NÃO tem como representar de forma interpretável, NÃO criar REPR!      

    ## HERANÇA ##
    class Student(Person): #Student recebeu de herança(Inheritance), os atributos e métodos de Person
        pass    
    #CASO QUEIRA TER OS ATRIBUTOS DE PEARSON + ATRIBUTOS NOVOS, podemos fazer de 2 maneiras:
    class Student(Person):
        def __init__(self, name, age, gradYear): #Inicia esta classe
            Person.__init__(name, age) #Chama construtor da classe herdada
            self.graduationyear = gradYear #Pode adicionar mais atributos a classe se quiser
    #OU
    class Student(Person):
        def __init__(self, name, age, gradYear):
            super().__init__(name, age) #Chama construtor(es) da(s) classe(s) herdada(s)
            self.graduationyear = gradYear #Pode adicionar mais atributos a classe se quiser
    
    
    p1 = Person("John", 36) #Criando instância de classe
    p1.name = "Fred" #Modificando atributo
    

    ## ITERADORES ##
    mystr = "banana"
    myit = iter(mystr) #Iter retorna o endereço da primeira iteração

    print(next(myit)) #'b'
    print(next(myit)) #'a'
    print(next(myit)) #'n'
    print(next(myit)) #'a'
    print(next(myit)) #'n'
    print(next(myit)) #'a'
    
    #COMO FAZER UM ITERADOR PARA UTILIZAR UM OBJETO COM LOOP FOR
    class MyNumbers:
      def __iter__(self):
        self.a = 1
        return self
      def __next__(self):
        if self.a <= 20:
          x = self.a
          self.a += 1
          return x
        else:
          raise StopIteration

    for x in MyNumbers(): #O loop 'FOR' cria um objeto iterador, e executa um metodo next() em cada loop
      print(x)
    
# EXTRAS  ####################################################################################

    if (__name__=="__main__"): -> Não executa o if se o código for importado
    
    x = abs(-7.25) #Retorna o valor positivo
    x = math.pi
    x = math.ceil(1.4) #Retorna o teto
    x = math.floor(1.4) #Retorna o chão
    len(objeto) #Retorna o tamanho daquele elemento
    
    try:  #Tenta fazer isso
    except: #Se der erro, "Except", faz isso
    raise Exception("Erro") #Mostra um erro na tela
    raise TypeError("Erro") #Mostra um erro na tela
    
    break, continue, e pass #Quebra loop, volta pro início do loop, e continua logo na linha abaixo

    x = valor<<n #Desloca os bits de 'valor'... 'n' vezes (&-e / |-ou / ^-ou exclusivo / ~-inversão)
 
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # Eleve os ímpares ao quadrado (List Comprehension)
    print [ x**2 for x in nums if x % 2 ]
    gen = ( x**2 for x in nums if x % 2 )
   
    if (isinstance(x, int)): #Bom para verificar o tipo de um dado

    from decimal import Decimal #Reduz o erro ao utilizar cálculos com ponto flutuante
    t = Decimal(str(5))
    for i in range(50):
        t-= Decimal(str(.1))
    
    from fractions import Fraction #Reduz o erro ao utilizar cálculos com frações
    f1 = Fraction('-2/3')
    f2 = Fraction(3, 4)
    f3 = Fraction('.25')
    print "Fraction('-2/3') =", f1
    print "Fraction('3, 4') =", f2
    print "Fraction('.25') =", f3
    
# Expressões regulares ########################################################################
    # Retornam o que contém nos grupos de busca, representados pelos parenteses ()

    #import re
    ^ $ #Procura no Início ou Fim da linha
    . #Pega todos os caracteres (menos \n)

    [] #São alternativas]
    [^abc] #Qualquer caractere menos "a" "b" ou "c'
    [.] = \. #Literalmente busca o ponto #sintaxe equivalente

    * + ? #Procura por: 0 ou mais, 1 ou mais , 0 ou 1
    {2,5} #Procura por 2 a 5 ocorrências
    {7} #Procura por 7 ocorrências

    | #Ou
    () #Grupo de busca, vai buscando por ordem dos parenteses, cada grupo é inserido em uma lista
    (?:) #Usado para não capturar esse grupo
    # \1 \2 \3 utilizado para acessar os grupos

    A (?=B) #Encontra expressão A que seja seguida de B
    A (?!B) #Encontra expressão A que NÃO seja seguida de B
    (?<=B) A #Encontra expressão A que seja antecedida de B
    (?<!B) A #Encontra expressão A que NÃO seja antecedida de B
    #Quando quiser utilizar mais de uma opção para isso, usar (?:(?<=A)|(?<=B))

    # \d -> [0-9]
    # \D -> [^0-9]

    # \s \S #Espaços de todos os tipos, NÃO espaços

    # \w -> [a-zA-Z0-9À-ú] 
    # \W -> [^a-zA-Z0-9À-ú] 

    FLAGS
    flags = re.A -> ascii #Não contém acentos se utilizar isso
    flags = re.I -> IGNORECASE #utilizando isso, tanto faz maíusculo ou mínusculo
    flags = re.M -> Multiline -> ^ $ #agora vale para cada linha, n só 1 vez para a string
    flags = re.S -> Dotall #Agora o "." vai pegar o \n também

    re.search("padrão ou RE","Vai buscar se o padrão está contido nesta string") #Busca uma ocorrência
    var.group() #PS: Para extrair o objeto usar:

    re.findall("padrão ou RE","Vai buscar se o padrão está contido nesta string") #Busca todas as ocorrências

    re.sub("regex", "substitui por isso", nessaString, NosPrimeirosXcasos) #Para substituir

    ex:
    import re
    string = "bjdgs  s laplace@gmail.com.br aasfk jjk akkka kj thales@naosei.br h pradomatheus@yahoo.br baide"
    lista = re.findall("([\w._-]*@[a-z]*\.(?:com\.br|com|br))",string)
    print(lista)