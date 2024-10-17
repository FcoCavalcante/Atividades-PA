#Acionando a biblioteca do Tkinter que permitirá o layout do app
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Janela tk
root = tk.Tk()
#Título do app
root.title("Calculadora de IMC")

#função que fará o cálculo do IMC
def calcular_imc(*args):
    # Solicita os dados do usuário
    try:
        #Cálculo do IMC
        peso = float(valor_peso.get().replace(',', '.'))
        altura = float(valor_altura.get().replace(',', '.'))
        imc = peso / (altura ** 2)
        
        #Exibição do resultado no rótulo
        label_resultado.config(text=f"Seu IMC é: {imc:.2f}")
        
        #Classificação
        classificacao = classificar_imc(imc)
        label_classificacao.config(text=f"Classificação: {classificacao}")        
    except ValueError:
        #Alerta de erro para o usuário
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

#Função de classificação do IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso. Procure um nutricionista."
    elif 18.5 <= imc < 24.9:
        return "Peso normal. Parabéns!"
    elif 25 <= imc < 29.9:
        return "Sobrepeso. Procure um nutricionista."
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1. Procure um médico."
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2. Procure um médico."
    else:
        return "Obesidade grau 3 (mórbida). Procure um médico urgente!"
    
#Criando o container <div></div>
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Rótulo e campo de entrada para o peso
ttk.Label(frame, text="Peso (kg):").grid(column=1, row=1, sticky=tk.W)
valor_peso = ttk.Entry(frame, width=7)
valor_peso.grid(column=2, row=1, sticky=(tk.W, tk.E))

# Rótulo e campo de entrada para a altura
ttk.Label(frame, text="Altura (m):").grid(column=1, row=2, sticky=tk.W)
valor_altura = ttk.Entry(frame, width=7)
valor_altura.grid(column=2, row=2, sticky=(tk.W, tk.E))

# Botão para calcular o IMC
ttk.Button(frame, text="Calcular", command=calcular_imc).grid(column=2, row=3, sticky=tk.W)

# Rótulo para exibir o resultado do IMC
label_resultado = ttk.Label(frame, text="Seu IMC é:")
label_resultado.grid(column=1, row=4, columnspan=2, sticky=tk.W)

# Rótulo para exibir a classificação do IMC
label_classificacao = ttk.Label(frame, text="Classificação:")
label_classificacao.grid(column=1, row=5, columnspan=2, sticky=tk.W)

#Agora será ajustado quando o mouse passar sobre os botões e também 
# quando o usuário apertar enter para ativar o return da função.
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Coloca o foco no campo de entrada do peso
valor_peso.focus()
root.bind("<Return>", calcular_imc)

# Inicia o loop principal da interface gráfica
root.mainloop()
