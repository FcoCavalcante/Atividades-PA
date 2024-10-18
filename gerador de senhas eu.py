import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import string

def gerar_senha(*args):
    #conjuntos de caracteres permitidos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #gerador de senhas
    senha = ''.join(random.choice(caracteres) for _ in range(8))
    #Saída de dados
    gerar.set(senha) 

# janela tk + Título do app
root = tk.Tk()
root.title("Gerador de Senhas")


#Criando o container
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

#Colunas e linhas
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

gerar = StringVar()
# Caixa de texto para exibir a senha gerada
campo_senha = tk.Text(frame, height=1, width=30, wrap=tk.WORD, state='normal')
campo_senha.grid(column=1, row=1, sticky=tk.W)
campo_senha.config(state='disabled')  # Desativa a edição, mas permite seleção

ttk.Label(frame, textvariable=gerar).grid(column=2, row=1, sticky=(tk.W, tk.E))
ttk.Button(frame, text="Gerar Senha", command=gerar_senha).grid(column=2, row=2, sticky=tk.W)

#efeito mouse
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

#enter
root.bind("<Retun>", gerar_senha())

#loop
root.mainloop()