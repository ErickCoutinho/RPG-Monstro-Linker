import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = 'd20pfsrd-Bestiary - Updated 23Feb2014.csv'
df_path = pd.read_csv(data)


'CORRELAÇÃO ENTRE ATRIBUTOS'
###########################################################################
columns_to_replace = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
for col in columns_to_replace:
    df_path[col] = df_path[col].replace('-', np.nan)
############################################################################

import seaborn as sns
atributos_principais = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
correlacao_atributos = df_path[atributos_principais].corr()
# Plotar um mapa de calor da matriz de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(correlacao_atributos, annot=True, cmap='coolwarm', linewidths=1)
plt.title('Matriz de Correlação entre Atributos Principais')
plt.show()
print(correlacao_atributos)




"XP obtido por nivel de CR"
###################################################################
df_path['XP'] = df_path['XP'].str.replace(',', '').astype(float)
###################################################################
# Filtrar o DataFrame para incluir apenas CR de 1 a 12
df_filtrado = df_path[df_path['CR'].between(1, 12)]

media_xp_por_cr = df_filtrado.groupby('CR')['XP'].mean()
plt.figure(figsize=(12, 6))
media_xp_por_cr.plot(kind='bar', color='red', alpha=0.7)
plt.xlabel('CR')
plt.ylabel('Média de XP')
plt.title('Média de XP por CR (CR de 1 a 12)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()






"PREVISÃO DE CR DE ACORDDO COM ESTATISTICAS BASICAS"
##############################################################
"""from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Selecionar os atributos físicos e a variável alvo
atributos_fisicos = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
X = df_path[atributos_fisicos]
y = df_path['CR']
X = X.dropna()
y = y[X.index]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
# Previsões para novas criaturas (forneça valores numéricos)
nova_criatura = pd.DataFrame({
    'Str': [16],
    'Dex': [14],
    'Con': [18],
    'Int': [12],
    'Wis': [10],
    'Cha': [8]
})
previsao_cr = model.predict(nova_criatura)
print(f"Previsão de CR para a nova criatura: {previsao_cr[0]}")"""
###########################################################################

"""from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

atributos_fisicos = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
X = df_path[atributos_fisicos]
y = df_path['CR']
X = X.dropna()
y = y[X.index]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

import tkinter as tk
from tkinter import ttk
from sklearn.linear_model import LinearRegression
from tkinter import PhotoImage
from PIL import Image, ImageTk

def prever_cr():
    # Obter os valores dos atributos da interface
    str_val = int(str_var.get())
    dex_val = int(dex_var.get())
    con_val = int(con_var.get())
    int_val = int(int_var.get())
    wis_val = int(wis_var.get())
    cha_val = int(cha_var.get())

    atributos = [[str_val, dex_val, con_val, int_val, wis_val, cha_val]]
    previsao_cr = model.predict(atributos)
    resultado_label.config(text=f"Previsão de CR: {previsao_cr[0]:.2f}")
model = LinearRegression()
model.fit(X_train, y_train)
root = tk.Tk()
root.title("Previsão de CR para Nova Criatura")
# Carregue a imagem e redimensione
background_image = Image.open("C:\\Users\\Erick Coutinho\\OneDrive\\Área de Trabalho\\FACULDADE\\PROJETO_INTEGRADOR I\\venv\\skyrim.png")
background_image = background_image.resize((2560, 1080))  # Substitua largura_desejada e altura_desejada pelos valores desejados
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)


font_size = 20
font = ("MedievalSharp", font_size)

str_var = tk.StringVar()
dex_var = tk.StringVar()
con_var = tk.StringVar()
int_var = tk.StringVar()
wis_var = tk.StringVar()
cha_var = tk.StringVar()

str_label = ttk.Label(root, text="Força (Str):", font=font)
str_label.grid(row=0, column=0)
str_entry = ttk.Entry(root, textvariable=str_var, font=font, width=10)
str_entry.grid(row=0, column=1)

dex_label = ttk.Label(root, text="Destreza (Dex):", font=font)
dex_label.grid(row=1, column=0)
dex_entry = ttk.Entry(root, textvariable=dex_var, font=font, width=10)
dex_entry.grid(row=1, column=1)

con_label = ttk.Label(root, text="Constituição (Con):", font=font)
con_label.grid(row=2, column=0)
con_entry = ttk.Entry(root, textvariable=con_var, font=font, width=10)
con_entry.grid(row=2, column=1)

int_label = ttk.Label(root, text="Inteligência (Int):", font=font)
int_label.grid(row=3, column=0)
int_entry = ttk.Entry(root, textvariable=int_var, font=font, width=10)
int_entry.grid(row=3, column=1)

wis_label = ttk.Label(root, text="Sabedoria (Wis):", font=font)
wis_label.grid(row=4, column=0)
wis_entry = ttk.Entry(root, textvariable=wis_var, font=font, width=10)
wis_entry.grid(row=4, column=1)

cha_label = ttk.Label(root, text="Carisma (Cha):", font=font)
cha_label.grid(row=5, column=0)
cha_entry = ttk.Entry(root, textvariable=cha_var, font=font, width=10)
cha_entry.grid(row=5, column=1)

style = ttk.Style()
fonte_botao = ("MedievalSharp", 20)
style.configure("TButton", font=fonte_botao)
prever_button = ttk.Button(root, text="Prever CR", command=prever_cr, style="TButton")
prever_button.grid(row=6, columnspan=2, padx=20, pady=20)
resultado_label = ttk.Label(root, text="",font=("MedievalSharp", 20) )
resultado_label.grid(row=7, columnspan=2)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()

"""