#Acionando a biblioteca do Tkinter que permiitirá o layout do app
from tkinter import *
from tkinter import ttk

#Janela tk
root = Tk()
#Título do app
root.title("Pés para Metros")

#função que fará o cálculo de conversão de pés para metros
def calculate(*args):
    try:
        value = float(feet.get()) #Entrada de dados
        result = int(0.3048 * value * 10000.0 + 0.5)/10000.0 #Processamento de dados
        meters.set(result) #Saída de dados
    except ValueError:
        pass

#Criando o container <div></div>
mainframe = ttk.Frame (root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#<input /> "pés"
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

#Input "metros"
meters = StringVar()                      #onde há "grid" significa a localização/layout
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=2, row=3, sticky=W)

#Label = "rótulo". Neste caso indicaremos onde ficará localizado na janela/layout
ttk.Label(mainframe, text="Pés").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Metros").grid(column=3, row=2, sticky=W)

#Agora será ajustado quando o mouse passar sobre os botões e também 
# quando o usuário apertar enter para ativar o return da função.
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

#Loop para renderização intermitente
root.mainloop()
