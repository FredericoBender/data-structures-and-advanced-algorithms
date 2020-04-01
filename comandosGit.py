git add arquivo #Adiciona arquivo no repositório local
git reset HEAD arquivo #Remove o arquivo do repositório local
git status #Para ver situação das mudanças
git commit -m "comentario" #Prepara o repositório local para envio
git push #Envia as modificações para o GitHub
git commit --amend #Para modificar o comentário do ultimo commit
git pull #Baixa as modificações do GitHub feitas por outros

git branch esseai #Para criar um branch chamado esseai
git branch -d esseai #Para deletar o branch esseai
git branch #Verifica o ramo que ele esta
git checkout qualbranch #Para mudar para essa ramificação. Pode ser usado para navegar nos commits
git merge qualbranch #Puxa os dados deste qualbranch e mescla com o atual

git stash #Salva as mudanças sem commitar para poder mudar de branch por exemplo
git stash list #Mostra a pilha de Stash's
git stash pop #Remove e pega  o último stash feito de volta

git log #Mostra os commits que foram feitos
git diff commitX commitY #Mostra as diferenças entre esses 2

git tag nomedaTag #Cria uma TAG / versão estável do meu software
git push origin nomedaTag #Envia TAG para o GitHUB

git config --global credential.helper cache #Salva o usuário do git no PC
git init #Cria o repositório onde o git vai salvar os commits

"""Criar arquivo .gitignore :
 se escrever nele diretorio/ --> Não vai commitar nada dentro disso, ou
 *.bak --> Não vai commitar nem um arquivo com a extensão .bak"""