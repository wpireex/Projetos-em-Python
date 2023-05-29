from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Criar nossa janela
jan = Tk()
jan.title("Acesso ao Painel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)

# Logo da empresa
logo = PhotoImage(file="Imagens/logo-ptt.png")  # Altere o caminho para a nova imagem do logo
logo = logo.subsample(3)  # Reduzir o tamanho da imagem pela metade


# Widgets
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=400, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=5, y=50)  # Ajuste a posição do logo conforme necessário

UserLabel = Label(RightFrame, text="Username", font=("Tahoma", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=50, y=100)  # Ajuste a posição do rótulo do username conforme necessário

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=200, y=110)  # Ajuste a posição do campo de entrada do username conforme necessário

PassLabel = Label(RightFrame, text="Password", font=("Tahoma", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=50, y=150)  # Ajuste a posição do rótulo da senha conforme necessário

PassEntry = ttk.Entry(RightFrame, width=30, show="*")  # Ocultar a senha com asteriscos
PassEntry.place(x=200, y=160)  # Ajuste a posição do campo de entrada da senha conforme necessário

# Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=15)
LoginButton.place(x=50, y=220)  # Ajuste a posição do botão de login conforme necessário

def Register():
    #removendo widhets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #Inserindo widgets de Cadastro

    NomeLabel = Label(RightFrame, text="Name:", font=("Tahoma", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)

    NomeEntry =Entry(RightFrame, width=30)
    NomeEntry.place(x=100, y=18)

RegisterButton = ttk.Button(RightFrame, text="Register", width=15, command=Register)
RegisterButton.place(x=150, y=220)  # Ajuste a posição do botão de registro conforme necessário

jan.mainloop()