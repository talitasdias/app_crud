import tkinter.ttk
from tkinter import messagebox
import customtkinter
import sqlite3
from tkinter import *

app = customtkinter.CTk()
app.title('Sistema de Funcionário')
app.geometry('800x500')
app.config(bg='#17043d')

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 15, 'bold')
font3 = ('Arial', 12, 'bold')

frame1 = customtkinter.CTkFrame(app, fg_color="#fff", width=450)
frame1.pack(side='right', fill='y')

db = sqlite3.connect('Funcionarios.db')
db.execute("CREATE TABLE IF NOT EXISTS FUNCIONARIO (Funcionario_ID Integer, Nome Text, Idade Text, Funcao Text)")
cursor = db.cursor()


def inserir():
    if (id_entry.get() == '' or nome_entry.get() == '' or idade_entry.get() == '' or funcao_entry.get() == ''):
        messagebox.showerror(title='Erro', message='Por favor preencha todos os dados.')
    else:
        detalhes = [int(id_entry.get()), nome_entry.get(), idade_entry.get(), funcao_entry.get()]
        cursor.execute("INSERT INTO Funcionario values(?,?,?,?)", detalhes)
        db.commit()
        messagebox.showinfo(title='Inserido', message='Funcionário foi inserido.')
        limpar()
        mostrar_dados()


def limpar():
    id_entry.delete(0, END)
    nome_entry.delete(0, END)
    idade_entry.delete(0, END)
    funcao_entry.delete(0, END)


def buscar():
    cursor.execute("SELECT * FROM Funcionario")
    linhas = cursor.fetchall()
    return linhas


def mostrar_dados():
    tv.delete(*tv.get_children())
    for linha in buscar():
        tv.insert("", END, values=linha)


def deletar():
    cursor.execute("DELETE FROM Funcionario WHERE Funcionario_ID=?", [id_entry.get()])
    db.commit()
    messagebox.showinfo(title='Deletado', message='Funcionário foi deletado.')
    mostrar_dados()
    limpar()


def pegar_dado(evento):
    limpar()
    linha_selecionada = tv.focus()
    dado = tv.item(linha_selecionada)
    linha = dado['values']
    if len(linha) != 0:
        id_entry.insert(0, linha[0])
        nome_entry.insert(0, linha[1])
        idade_entry.insert(0, linha[2])
        funcao_entry.insert(0, linha[3])


def atualizar():
    novos_detalhes = [nome_entry.get(), idade_entry.get(), funcao_entry.get(), int(id_entry.get())]
    cursor.execute("UPDATE Funcionario set Nome=?, Idade=?, Funcao=? WHERE Funcionario_ID=?", novos_detalhes)
    db.commit()
    messagebox.showinfo(title='Atualizado', message='Informações do funcionário atualizadas.')
    mostrar_dados()
    limpar()


id_label = customtkinter.CTkLabel(app, text='ID:', font=font1, fg_color='#17043d', bg_color='#17043d', text_color='#fff')
id_label.place(x=20, y=20)
id_entry = customtkinter.CTkEntry(app, font=font2, text_color='#000', fg_color='#fff', border_color='#fff', bg_color='#17043d', corner_radius=40, width=200)
id_entry.place(x=140, y=20)

nome_label = customtkinter.CTkLabel(app, text='Nome:', font=font1, fg_color='#17043d', bg_color='#17043d', text_color='#fff')
nome_label.place(x=20, y=80)
nome_entry = customtkinter.CTkEntry(app, font=font2, text_color='#000', fg_color='#fff', border_color='#fff', width=200, bg_color='#17043d', corner_radius=40)
nome_entry.place(x=140, y=80)

idade_label = customtkinter.CTkLabel(app, text='Idade:', font=font1, fg_color='#17043d', bg_color='#17043d', text_color='#fff')
idade_label.place(x=20, y=140)
idade_entry = customtkinter.CTkEntry(app, font=font2, text_color='#000', fg_color='#fff', border_color='#fff', width=200, bg_color='#17043d', corner_radius=40)
idade_entry.place(x=140, y=140)

funcao_label = customtkinter.CTkLabel(app, text='Função:', font=font1, fg_color='#17043d', bg_color='#17043d', text_color='#fff')
funcao_label.place(x=20, y=200)
funcao_entry = customtkinter.CTkEntry(app, font=font2, text_color='#000', fg_color='#fff', border_color='#fff', width=200, bg_color='#17043d', corner_radius=40)
funcao_entry.place(x=140, y=200)

salvar_botao = customtkinter.CTkButton(app, text='Salvar', font=font1, fg_color='#03a819', bg_color='#17043d', hover_color='#03a819', corner_radius=20, width=120, cursor='hand2', command=inserir)
salvar_botao.place(x=70, y=250)
atualizar_botao = customtkinter.CTkButton(app, text='Atualizar', font=font1, fg_color='#b86512', bg_color='#17043d', hover_color='#b86512', corner_radius=20, width=120, cursor='hand2', command=atualizar)
atualizar_botao.place(x=200, y=250)
limpar_botao = customtkinter.CTkButton(app, text='Limpar', font=font1, fg_color='#6e0e53', bg_color='#17043d', hover_color='#6e0e53', corner_radius=20, width=120, cursor='hand2', command=limpar)
limpar_botao.place(x=70, y=300)
deletar_botao = customtkinter.CTkButton(app, text='Deletar', font=font1, fg_color='#cf061a', bg_color='#17043d', hover_color='#cf061a', corner_radius=20, width=120, cursor='hand2', command=deletar)
deletar_botao.place(x=200, y=300)

estilo = tkinter.ttk.Style()
estilo.configure('meuestilo.Treeview', font=font3, rowheight=50)
estilo.configure('meuestilo.Treeview.Heading', font=font3)
estilo.layout('meuestilo.Treeview', [('meuestilo.Treeview.treearea', {'sticky': 'nswe'})])

tv = tkinter.ttk.Treeview(frame1, columns=(1, 2, 3, 4), show='headings', style='meuestilo.Treeview')
tv.heading('1', text='ID')
tv.column('1', width=105)
tv.heading('2', text='Nome')
tv.column('2', width=105)
tv.heading('3', text='Idade')
tv.column('3', width=105)
tv.heading('4', text='Função')
tv.column('4', width=105)
tv.bind('<ButtonRelease-1>', pegar_dado)

tv.pack()

mostrar_dados()

app.mainloop()
