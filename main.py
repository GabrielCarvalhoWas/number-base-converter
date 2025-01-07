
from tkinter import *
from tkinter import ttk



cor_0 = "#000000"  # cor preta
cor_1 = "#feffff"  # cor branca
cor_2 = "#6f9fbd"  # cor cinza para o botão
cor_3 = "#38576b"  # cinza escuro (fundo dos frames)
cor_4 = "#e0e0e0"  # cor cinza claro (fundo dos resultados)

# Configuração da janela principal
janela = Tk()
janela.title('Gabriel Pereira de Carvalho')
janela.geometry('400x310')
janela.configure(bg=cor_1)



style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

# divisão das frames
frame_cima = Frame(janela, width=400, height=60, bg=cor_1, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, bg=cor_3, pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)

# configuração do frame superior
app_nome = Label(
    frame_cima,
    text="Conversor de Base Numérica",
    relief=FLAT,
    anchor="center",
    font=("System", 16, "bold"),
    bg=cor_2,
    fg=cor_1,
)
app_nome.place(x=50, y=15)

def converter():
    def numero_para_decimal(numero, base):
        try:
            # Verificar se o valor não está vazio
            if not numero:
                raise ValueError("Input is empty!")

            decimal = int(numero, base)  
            binario = bin(decimal)[2:]   
            octal = oct(decimal)[2:]    
            hexadecimal = hex(decimal)[2:].upper()  

            # Atualizando os labels com os resultados
            l_binario_valor['text'] = binario
            l_octal_valor['text'] = octal
            l_decimal_valor['text'] = str(decimal)
            l_hexadecimal_valor['text'] = hexadecimal

        except ValueError:
            # Se houver erro de conversão (como número inválido ou vazio)
            l_binario_valor['text'] = "Invalid Input!"
            l_octal_valor['text'] = "Invalid Input!"
            l_decimal_valor['text'] = "Invalid Input!"
            l_hexadecimal_valor['text'] = "Invalid Input!"

    numero = e_valor.get()
    base = combo.get()
    
    if base == "binario":
        base = 2
    elif base == "octal":
        base = 8
    elif base == "decimal":
        base = 10
    elif base == "hexadecimal":
        base = 16

    numero_para_decimal(numero, base)

# Configurando o frame inferior
bases = ['binario', 'octal', 'decimal', 'hexadecimal']

combo = ttk.Combobox(frame_baixo, width=12, justify=CENTER, font=("Ivy 12 bold"))
combo['values'] = bases
combo.place(x=35, y=10)
combo.current(0)  # Seleciona a base inicial

e_valor = Entry(frame_baixo, width=9, justify='center', font=("", 13), highlightthickness=1, relief='solid')
e_valor.place(x=160, y=10)

botao_converter = Button(
    frame_baixo,
    command=converter,
    text="Convert",
    relief=RAISED,
    overrelief=RIDGE,
    font=("Ivy 8 bold"),
    bg=cor_2,
    fg=cor_1,
)
botao_converter.place(x=247, y=10)

# configaração dos labels
# binário
frame_binario = Frame(frame_baixo, bg=cor_3)
frame_binario.place(x=35, y=60)

l_binario_label = Label(frame_binario, text="Binário:         ", relief=FLAT, anchor="nw", font=("Verdana", 13), bg=cor_1, fg=cor_0)
l_binario_label.grid(row=0, column=0, padx=5)

l_binario_valor = Label(frame_binario, text="None", width=13, anchor="center", font=("Verdana", 13), bg=cor_1, fg=cor_0, borderwidth=1, relief="solid")
l_binario_valor.grid(row=0, column=1, padx=5)

# Octal
frame_octal = Frame(frame_baixo, bg=cor_3)
frame_octal.place(x=35, y=100)

l_octal_label = Label(frame_octal, text="Octal:           ", relief=FLAT, anchor="nw", font=("Verdana", 13), bg=cor_1, fg=cor_0)
l_octal_label.grid(row=0, column=0, padx=5)

l_octal_valor = Label(frame_octal, text="None", width=13, anchor="center", font=("Verdana", 13), bg=cor_1, fg=cor_0, borderwidth=1, relief="solid")
l_octal_valor.grid(row=0, column=1, padx=5)

# Decimal
frame_decimal = Frame(frame_baixo, bg=cor_3)
frame_decimal.place(x=35, y=140)

l_decimal_label = Label(frame_decimal, text="Decimal:       ", relief=FLAT, anchor="nw", font=("Verdana", 13), bg=cor_1, fg=cor_0)
l_decimal_label.grid(row=0, column=0, padx=5)

l_decimal_valor = Label(frame_decimal, text="None", width=13, anchor="center", font=("Verdana", 13), bg=cor_1, fg=cor_0, borderwidth=1, relief="solid")
l_decimal_valor.grid(row=0, column=1, padx=5)

# Hexadecimal
frame_hexadecimal = Frame(frame_baixo, bg=cor_3)
frame_hexadecimal.place(x=35, y=180)

l_hexadecimal_label = Label(frame_hexadecimal, text="Hexadecimal:", relief=FLAT, anchor="nw", font=("Verdana", 13), bg=cor_1, fg=cor_0)
l_hexadecimal_label.grid(row=0, column=0, padx=5)

l_hexadecimal_valor = Label(frame_hexadecimal, text="None", width=13, anchor="center", font=("Verdana", 13), bg=cor_1, fg=cor_0, borderwidth=1, relief="solid")
l_hexadecimal_valor.grid(row=0, column=1, padx=5)

janela.mainloop()