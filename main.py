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

salvar_botao = customtkinter.CTkButton(app, text='Salvar', font=font1, fg_color='#03a819', bg_color='#17043d', hover_color='#03a819', corner_radius=20, width=120, cursor='hand2')
salvar_botao.place(x=70, y=250)

atualizar_botao = customtkinter.CTkButton(app, text='Atualizar', font=font1, fg_color='#b86512', bg_color='#17043d', hover_color='#b86512', corner_radius=20, width=120, cursor='hand2')
atualizar_botao.place(x=200, y=250)

limpar_botao = customtkinter.CTkButton(app, text='Limpar', font=font1, fg_color='#6e0e53', bg_color='#17043d', hover_color='#6e0e53', corner_radius=20, width=120, cursor='hand2')
limpar_botao.place(x=70, y=300)

deletar_botao = customtkinter.CTkButton(app, text='Deletar', font=font1, fg_color='#cf061a', bg_color='#17043d', hover_color='#cf061a', corner_radius=20, width=120, cursor='hand2')
deletar_botao.place(x=200, y=300)

app.mainloop()
