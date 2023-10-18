from cgitb import text
from tkinter import * 
import tkinter as tk 
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from banco import *
from tkinter import messagebox

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

personalizado = "#191970"
################# cores ############### 

#criando janela

janela = tk.Tk()

janela.title ("Atividade tkinter Enilda")

janela.geometry("")
janela.configure(background=co9) 
janela.resizable(width=FALSE,height=FALSE) #aqui está bloqueando modificar o tamanho da tela 

#dividindo janela ! 

frame_cima = Frame(janela,width=310,height=50,bg=co2,relief='flat')
frame_cima.grid(row=0,column=0) 

frame_baixo = Frame(janela,width=310,height=403,bg=co1,relief='flat')
frame_baixo.grid(row=1,column=0,sticky=NSEW,padx=0,pady=1) 

frame_direita = Frame(janela,width=588,height=403,bg=co1,relief='flat')
frame_direita.grid(row=0,column=1,rowspan=2,padx=1,pady=0,sticky=NSEW) 

############ Label Cima ####################
global tree



app_nome = Label(frame_cima,text='Formulario',anchor=NW,font=('Ivy 16 bold'),bg=co2,fg=co1,relief='flat')

app_nome.place(x=16,y=13)  

def insert_dados():
    x=banco
    nome=e_nome.get()
    email=e_email.get()
    tel=e_telefone.get()
    dia=e_calendario.get()
    estado=e_estado.get()
    assunto=e_assunto.get()
    
    lista=[nome,email,tel,dia,estado,assunto]
    
    if nome=='':
        messagebox.showerror('erro','nome nao pode ser vazio')
    else:
        
        
        x=banco
        x.cadastro(lista)    
        messagebox.showinfo('Sucesso','cadastrado com sucesso')  
        
        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_calendario.delete(0,'end')
        e_estado.delete(0,'end')
        e_assunto.delete(0,'end')

       
    
    for widget in frame_direita.winfo_children():
        widget.destroy()
    
    
    mostrar()    





def atualizar ():
    try :
        treev_dados=tree.focus()
        treev_dicionario=tree.item(treev_dados)
        tree_lista=treev_dicionario['values']
        
        valor_id = tree_lista[0]
        
        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_calendario.delete(0,'end')
        e_estado.delete(0,'end')
        e_assunto.delete(0,'end')
        
        
        
        e_nome.insert(0,tree_lista[1])
        e_email.insert(0,tree_lista[2])
        e_telefone.insert(0,tree_lista[3])
        e_calendario.insert(0,tree_lista[4])
        e_estado.insert(0,tree_lista[5])
        e_assunto.insert(0,tree_lista[6])


        
        def atualizar_dados():
            x=banco
            nome=e_nome.get()
            email=e_email.get()
            tel=e_telefone.get()
            dia=e_calendario.get()
            estado=e_estado.get()
            assunto=e_assunto.get()
            
            lista=[nome,email,tel,dia,estado,assunto,valor_id]
            
            if nome=='':
                messagebox.showerror('erro','nome nao pode ser vazio')
            else:
                
                
                x=banco
                x.atualiza_info(lista)   
                messagebox.showinfo('Sucesso','dados atualizados com sucesso')  
                
                e_nome.delete(0,'end')
                e_email.delete(0,'end')
                e_telefone.delete(0,'end')
                e_calendario.delete(0,'end')
                e_estado.delete(0,'end')
                e_assunto.delete(0,'end')

            
            
            for widget in frame_direita.winfo_children():
                widget.destroy()
            mostrar()   
                
        b_confirmar = Button(frame_baixo, text='Confirmar', command=atualizar_dados, width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')

        b_confirmar.place(x=110, y=370)
                    


             
        
                 
    except IndexError:
        messagebox.showerror('erro','escolha uma tabela')
 
 
 
 
 
 
      





############ Criando Frame baixo ####################

#Input NOME
l_nome = Label(frame_baixo,text=' nome *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_nome.place(x=10,y=10)
e_nome = Entry(frame_baixo,width=45,justify='left',relief='solid')
e_nome.place(x=15,y=40)

#Input Email
l_email = Label(frame_baixo,text=' Email *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_email.place(x=10,y=70)
e_email = Entry(frame_baixo,width=45,justify='left',relief='solid')
e_email.place(x=15,y=100)

#Input TELEFONE
l_telefone = Label(frame_baixo,text=' Telefone *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_telefone.place(x=10,y=140)
e_telefone = Entry(frame_baixo,width=45,justify='left',relief='solid')
e_telefone.place(x=15,y=170)

#Input Estado
l_estado = Label(frame_baixo,text=' Estado *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_estado.place(x=164,y=200)
e_estado = Entry(frame_baixo,width=20,justify='left',relief='solid')
e_estado.place(x=164,y=230) 

#Input DATA
l_calendario = Label(frame_baixo,text=' Data *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_calendario.place(x=10,y=200)
e_calendario = DateEntry(frame_baixo,width=15,background='darkblue',foreground='white',borderwidth=2)
e_calendario.place(x=15,y=230)

#sobre 
l_assunto = Label(frame_baixo,text=' Sobre *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4,relief='flat')
l_assunto.place(x=10,y=260)
e_assunto = Entry(frame_baixo,width=45,justify='left',relief='solid')
e_assunto.place(x=15,y=290)

#botão Insert 

# b_inserir = Button(frame_baixo,command=insert_dados,text='Cadastrar',width=10,font=('Ivy 9 bold'), bg=co2,fg=co1,relief='raised',overrelief='ridge')




b_inserir = Button(frame_baixo, command=insert_dados, text='Cadastrar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=209, y=340)

#botão Update

b_atualizar = Button(frame_baixo,text='Atualizar',width=10,command=atualizar,font=('Ivy 9 bold'), bg=co6,fg=co1,relief='raised',overrelief='ridge')
b_atualizar.place(x=110, y=340)

#botão Deletar

b_deletar = Button(frame_baixo,text='Deletar',width=10,font=('Ivy 9 bold'), bg=co7,fg=co1,relief='raised',overrelief='ridge')
b_deletar.place(x=15, y=340)

#Frame da direita 

# lista = [[1,'Joao Futi Muanda','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
#            [2,'Fortnato Mpngo', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
#            [3,'Usando Python',  'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
#            [4,'Clinton Berclidio', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente'],
#            [5,'A traicao da Julieta','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente']
#            ]


def mostrar():
    x=banco
    
    global tree 
    
    lista=x.mostrar_dados()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']

    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

mostrar()
janela.mainloop() 