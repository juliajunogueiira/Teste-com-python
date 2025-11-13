import tkinter as tk

# Funções para mudar as cores
def mudar_esquerda_verde(event=None):
    canvas.itemconfig(metade_esquerda, fill="blue")

def mudar_direita_verde(event=None):
    canvas.itemconfig(metade_direita, fill="red")

def resetar_cores(event=None):
    canvas.itemconfig(metade_esquerda, fill="black")
    canvas.itemconfig(metade_direita, fill="black")

# Função para encerrar o programa
def encerrar_programa(event=None):
    janela.destroy()

# Janela principal
janela = tk.Tk()
janela.title("Tela interativa")
janela.attributes("-fullscreen", True)  # Ativa modo tela cheia

# Obter dimensões da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Canvas ocupando toda a tela, sem bordas
canvas = tk.Canvas(
    janela,
    width=largura_tela,
    height=altura_tela,
    highlightthickness=0,
    bd=0
)
canvas.pack()

# Criar metades perfeitamente igualadas
metade_esquerda = canvas.create_rectangle(
    0, 0,
    largura_tela // 2, altura_tela,
    fill="black"
)

metade_direita = canvas.create_rectangle(
    largura_tela // 2, 0,
    largura_tela, altura_tela,
    fill="black"
)

# Vincular teclas
janela.bind("<KeyPress-a>", mudar_esquerda_verde)
janela.bind("<KeyPress-d>", mudar_direita_verde)
janela.bind("<KeyPress-s>", resetar_cores)
janela.bind("<Escape>", encerrar_programa)

# Iniciar interface
janela.mainloop()
#
