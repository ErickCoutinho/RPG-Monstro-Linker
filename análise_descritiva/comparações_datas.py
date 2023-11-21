import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fractions import Fraction
import re


#PREPROCESSAMENTO ###########################################################################
data1 = 'dnd_monsters.csv'
df = pd.read_csv(data1)
colunas_excluir = ['url', 'speed']
df = df.drop(columns= colunas_excluir)
df = df.dropna(subset=['str', 'dex', 'con', 'int', 'wis', 'cha'], how='all')
df = df.reset_index(drop=True)
data2 = 'dnd_monsters.csv_2'
df.to_csv(data2)
df_dd = pd.read_csv('dnd_monsters.csv_2')
data = 'd20pfsrd-Bestiary - Updated 23Feb2014.csv'
df_path = pd.read_csv(data)
df_path['XP'] = df_path['XP'].str.replace(',', '').astype(float)
columns_to_replace = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
for col in columns_to_replace:
    df_path[col] = df_path[col].replace('-', np.nan)
cols_to_convert = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
df_path[cols_to_convert] = df_path[cols_to_convert].apply(pd.to_numeric, errors='coerce')
df_path = df_path.dropna(subset=cols_to_convert)
data3 = 'Tagmar - Criaturas.csv'
df_tagmar = pd.read_csv(data3, encoding='latin1', delimiter=';')
df_tagmar.dropna(subset=["Est"], inplace=True)

###################################################################################################


tipos_de_criaturas = ['dragon', 'undead', 'aberration']

# Inicializar listas para armazenar as médias
medias_dd = []
medias_path = []

# Calcular as médias das estatísticas básicas para cada tipo de criatura em D&D e Pathfinder
for tipo in tipos_de_criaturas:
    medias_dd.append(df_dd[df_dd['type'] == tipo][['str', 'dex', 'con', 'int', 'wis', 'cha']].mean())
    medias_path.append(df_path[df_path['Type'] == tipo][['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']].mean())

# Criar DataFrames de comparação para cada tipo de criatura
comparacao_dragon = pd.DataFrame({'D&D': medias_dd[0], 'Pathfinder': medias_path[0]})
comparacao_undead = pd.DataFrame({'D&D': medias_dd[1], 'Pathfinder': medias_path[1]})
comparacao_aberration = pd.DataFrame({'D&D': medias_dd[2], 'Pathfinder': medias_path[2]})

# Plotar os gráficos de barras comparativos para cada tipo de criatura
fig, axs = plt.subplots(figsize=(8, 6))
comparacao_dragon.plot(kind='bar', ax=axs, color=['red', 'blue'], legend=True)
axs.set_title('Comparação das Médias das Estatísticas Básicas para Dragões (D&D vs Pathfinder)', fontsize=10)
axs.set_ylabel('Média', fontsize=10)
axs.tick_params(axis='x', rotation=0, labelsize=8)
axs.tick_params(axis='y', labelsize=8)
plt.tight_layout()
plt.show()

# Gráfico para Mortos-Vivos (D&D vs Pathfinder)
fig, axs = plt.subplots(figsize=(8, 6))
comparacao_undead.plot(kind='bar', ax=axs, color=['red', 'blue'], legend=False)
axs.set_title('Comparação das Médias das Estatísticas Básicas para Mortos-Vivos (D&D vs Pathfinder)', fontsize=10)
axs.set_ylabel('Média', fontsize=10)
axs.tick_params(axis='x', rotation=0, labelsize=8)
axs.tick_params(axis='y', labelsize=8)
plt.tight_layout()
plt.show()

# Gráfico para Aberrações (D&D vs Pathfinder)
fig, axs = plt.subplots(figsize=(8, 6))
comparacao_aberration.plot(kind='bar', ax=axs, color=['red', 'blue'], legend=False)
axs.set_title('Comparação das Médias das Estatísticas Básicas para Aberrações (D&D vs Pathfinder)', fontsize=10)
axs.set_ylabel('Média', fontsize=10)
axs.tick_params(axis='x', rotation=0, labelsize=8)
axs.tick_params(axis='y', labelsize=8)
plt.tight_layout()
plt.show()

#CAUSA DAS CRIATURAS EM PATHFINDER serem mais fortes: ele permite ir ate o nivel 20


##########################################################################################################

fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico para D&D
cr_counts_dd = df_dd['cr'].value_counts().sort_index()
cr_levels_dd = sorted(cr_counts_dd.index, key=lambda x: Fraction(x).limit_denominator())
axs[0].bar(cr_levels_dd, cr_counts_dd[cr_levels_dd], color='blue')
axs[0].set_title('Quantidade de Criaturas por Nível de CR (D&D)')
axs[0].set_xlabel('Nível de CR')
axs[0].set_ylabel('Quantidade de Criaturas')

# Gráfico para Pathfinder
cr_counts_pathfinder = df_path['CR'].value_counts().sort_index()
cr_levels_pathfinder = sorted(cr_counts_pathfinder.index, key=lambda x: Fraction(x).limit_denominator())
axs[1].bar(cr_levels_pathfinder, cr_counts_pathfinder[cr_levels_pathfinder], color='red')
axs[1].set_title('Quantidade de Criaturas por Nível de CR (Pathfinder)')
axs[1].set_xlabel('Nível de CR')
axs[1].set_ylabel('Quantidade de Criaturas')

# Ajuste o layout e mostre os gráficos
plt.tight_layout()
plt.show()

############################################################################################################################
'COMAPRAÇÃO D&D E TAGMAR'


# Função para converter frações em decimais
def converter_fracao_em_decimal(fracao):
    if isinstance(fracao, float):
        return fracao
    partes = re.findall(r'\d+', fracao)
    if len(partes) == 2:
        numerador, denominador = map(int, partes)
        return numerador / denominador
    elif len(partes) == 1:
        return float(partes[0])
    else:
        return float('NaN')

# Aplicar a função de conversão à coluna "Est"
df_tagmar['Est'] = df_tagmar['Est'].apply(converter_fracao_em_decimal)
df_dd['cr'] = df_dd['cr'].apply(converter_fracao_em_decimal)
# Calculando as médias
media_est_tagmar = df_tagmar["Est"].mean()
media_cr_dd = df_dd["cr"].mean()
df_medias = pd.DataFrame({"Jogo": ["Tagmar", "D&D"], "Média": [media_est_tagmar, media_cr_dd]})
# Criando um gráfico de barras para comparar as médias
plt.figure(figsize=(8, 6))
plt.bar(df_medias["Jogo"], df_medias["Média"], color=["blue", "green"])
plt.title("Comparação das Médias de 'Est' e 'cr'")
plt.xlabel("Jogo")
plt.ylabel("Média")
plt.show()

#HISTOGRAMA TAGMAR
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df_tagmar['Est'], bins=15, color='skyblue', edgecolor='black')
plt.title('Histograma de Est em Tagmar')
plt.xlabel('Est')
plt.ylabel('Frequência')
# Histograma para D&D
plt.subplot(1, 2, 2)
plt.hist(df_dd['cr'], bins=15, color='salmon', edgecolor='black')
plt.title('Histograma de cr em D&D')
plt.xlabel('cr')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()