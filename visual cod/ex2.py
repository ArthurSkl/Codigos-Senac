Nsalto=5
nomes=("")
saltos=0
saltos1=[]
media=0
nss=[]
op=0
while True:
    n=input("qual nome do atleta ? ")
   
    nss.append(n)

    for i in range(5):
        s=int(input("digite a distacia exata do salto ! "))
        saltos1.append(s)
        nss.append(s)

    # x=(saltos.index(max(saltos)))
    # print(x)
    # x1=(saltos.index(min(saltos)))
    # print(x1)

    # del saltos[x]
    # del saltos[x1] 
    print("TESTE SALTOS === ",saltos1)

    media=(sum(saltos1)/3)
    print("media = ",media)
    nss.append(media)

    

    
    op=int(input("parar "))

    for i in range(len(nss)):
        print("posição 1 ",nss[1])
        


    if(op==1): 
        for i in range (len(nss)):
            print("TESTE COISAS",nss[i])
        
        for c, v in enumerate(saltos1):
            print(f"Na posição {c} encontrei o valor{v}!")
        print("cheguei ao final da lista. ")    
        break