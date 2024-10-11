#Acionando a biblioteca do Tkinter que permiitirá o layout do app
from tkinter import *
from tkinter import ttk

#Janela tk
root = Tk()
#Título do app
root.title("Milhas para Km")

#função que fará o cálculo de conversão de milhas para quilômetros
def calculate(*args):
    try:
        value = float(milhas.get()) #Entrada de dados
        result = int(value * 1.6) #Processamento de dados
        km.set(result) #Saída de dados
    except ValueError:
        pass

#Criando o container <div></div>
mainframe = ttk.Frame (root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#<input /> "milhas"
milhas = StringVar()
milhas_entry = ttk.Entry(mainframe, width=7, textvariable=milhas)
milhas_entry.grid(column=2, row=1, sticky=(W, E))

#Saída "Km"
km = StringVar()                      #onde há "grid" significa a localização/layout
ttk.Label(mainframe, textvariable=km).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=2, row=3, sticky=W)

#Label = "rótulo". Neste caso indicaremos onde ficará localizado na janela/layout
ttk.Label(mainframe, text="Milhas").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Km").grid(column=3, row=2, sticky=W)

#Agora será ajustado quando o mouse passar sobre os botões e também 
# quando o usuário apertar enter para ativar o return da função.
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

milhas_entry.focus()
root.bind("<Return>", calculate)

#Loop para renderização intermitente
root.mainloop()
