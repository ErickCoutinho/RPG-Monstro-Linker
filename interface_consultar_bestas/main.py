import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
import pandas as pd

df = pd.read_csv('bd_bestas.csv')

def pesquisar_monstro():
    nome_monstro = entry.get()

    resultado_pesquisa = df[df['Tagmar'].str.lower() == nome_monstro.lower()]

    if not resultado_pesquisa.empty:
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"Resultado da Pesquisa:\n------------------------\n")
        resultado_text.insert(tk.END,
                              f"\nTagmar:\nNome: {resultado_pesquisa['Tagmar'].values[0]}\nDescrição: {resultado_pesquisa['descrição'].values[0]}\nAtributos: {resultado_pesquisa[['INT(tagmar)', 'AUR(tagmar)', 'CAR(tagmar)', 'FOR(tagmar)', 'FIS(tagmar)', 'AGI(tagmar)', 'PER(tagmar)']].values[0]}\n\n")
        resultado_text.insert(tk.END,
                              f"\nPathfinder:\nNome: {resultado_pesquisa['Pathfinder'].values[0]}\nAtributos: {resultado_pesquisa[['Str (Pathinder)', 'Dex (Pathinder)', 'Con (Pathinder)', 'Int (Pathinder)', 'Wis (Pathinder)', 'Cha (Pathinder)']].values[0]}\n\n")
        resultado_text.insert(tk.END,
                              f"\nD&D:\nNome: {resultado_pesquisa['D&D'].values[0]}\nAtributos: {resultado_pesquisa[['Str (D&D)', 'Dex (D&D)', 'Con (D&D)', 'Int (D&D)', 'Wis (D&D)', 'Cha (D&D)']].values[0]}\n")
        resultado_text.config(state=tk.DISABLED)
    else:
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "Monstro não encontrado. Tente novamente.")
        resultado_text.config(state=tk.DISABLED)


def on_entry_key_release(event):
    letra_digitada = entry.get().lower()

    monstros_filtrados = df[df['Tagmar'].str.lower().str.startswith(letra_digitada)]

    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)

    if not monstros_filtrados.empty:
        resultado_text.insert(tk.END, "Monstros que começam com '{}' :\n".format(letra_digitada.upper()))
        for nome_monstro in monstros_filtrados['Tagmar']:
            resultado_text.insert(tk.END, "- {}\n".format(nome_monstro))
    else:
        resultado_text.insert(tk.END, "Nenhum monstro encontrado com a letra '{}'.".format(letra_digitada.upper()))

    resultado_text.config(state=tk.DISABLED)

def on_entry_click(event):
    if entry.get() == "Digite aqui!":
        entry.delete(0, "end")
        entry.config(fg="black")

def on_entry_focusout(event):
    if not entry.get():
        entry.insert(0, "Digite aqui!")
        entry.config(fg="grey")

janela = tk.Tk()
janela.title("RPG MONSTER LINKER")
janela.geometry("600x600")

janela.iconbitmap("shield.ico")

imagem_fundo = Image.open("imgrpg.jpg")
imagem_fundo = imagem_fundo.resize((1920, 1080), PIL.Image.LANCZOS)
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

label_fundo = ttk.Label(janela, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Adiciona o título
titulo_label = ttk.Label(janela, text="RPG MONSTER LINKER", foreground="black", font=("Helvetica", 16, "bold"))
titulo_label.pack(pady=10)

entry_label = ttk.Label(janela, text="Digite o nome do monstro:", foreground="black", font=("Helvetica", 12))
entry_label.pack(pady=5)

entry = ttk.Entry(janela, width=30, font=("Helvetica", 12))
entry.insert(0, "Digite aqui!")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_entry_focusout)
entry.bind("<KeyRelease>", on_entry_key_release)
entry.pack(pady=10)

botao_pesquisar = ttk.Button(janela, text="Pesquisar", command=pesquisar_monstro)
botao_pesquisar.pack(pady=10)

resultado_text = tk.Text(janela, height=25, width=50, wrap=tk.WORD, font=("Arial", 10), background="#EAEAEA", borderwidth=3, relief="solid", padx=10, pady=10)
resultado_text.pack(pady=10)
resultado_text.config(state=tk.DISABLED)

label_fundo.image = imagem_fundo

janela.mainloop()
