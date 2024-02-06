dados=[]
soma=0
jovem=0
adulto=0
idoso=0
qnt=int(input("quantos alunos tem na sala ? "))
for i in range(qnt):
    nome=input("digite seu nome ? ")
    idade=int(input("digite sua idade !"))
    dados.append(nome)
    dados.append(idade)
    soma+=idade
    
media=soma/qnt
print(dados,"\n média dos alunos ""%.2f"%media)    
print(dados[0],dados[1])

if(media<=25):
    print("turma de jovens !")
elif(media<=60):
    print("turma de adultos !")
elif(media>60):
    print("turma de idosos !")
            