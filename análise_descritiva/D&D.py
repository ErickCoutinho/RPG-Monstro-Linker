import pandas as pd

data1 = 'dnd_monsters.csv'
df = pd.read_csv(data1)
colunas_excluir = ['url', 'speed']
df = df.drop(columns= colunas_excluir)

# Excluir as linhas em que todas as colunas 'str', 'dex', 'con', 'int', 'wis' e 'cha' sejam nulas
df = df.dropna(subset=['str', 'dex', 'con', 'int', 'wis', 'cha'], how='all')
df = df.reset_index(drop=True)
data2 = 'dnd_monsters.csv_2'
df.to_csv(data2)



from prettytable import PrettyTable

# Carregue o arquivo CSV em um DataFrame
df_dd = pd.read_csv('dnd_monsters.csv_2')
# Crie uma tabela
tabela = PrettyTable()
# Adicione os nomes das colunas como cabeçalhos da tabela
tabela.field_names = df.columns
# Adicione as linhas ao DataFrame à tabela
for _, row in df.head(10).iterrows():
    tabela.add_row(row)
# Exiba a tabela
print(tabela)


###########################################################



import matplotlib.pyplot as plt
"gráfico com a media de cada atributo principal para as raças"
# Tipos de criaturas que você deseja incluir no gráfico
tipos_criaturas = ['elemental', 'undead', 'plant', 'giant', 'celestial','humanoid (any race)','dragon']
# Filtrar o DataFrame para incluir apenas os tipos de criaturas mencionados
df_tipos_selecionados = df_dd[df_dd['type'].isin(tipos_criaturas)]
# Selecionar as colunas relevantes de atributos principais
atributos_principais = ['str', 'dex', 'con', 'int', 'wis', 'cha']
# Calcular a média de cada atributo principal para os tipos de criaturas selecionados
media_atributos_por_tipo = df_tipos_selecionados.groupby('type')[atributos_principais].mean()
# Plotar o gráfico de barras agrupadas com os atributos principais lado a lado
media_atributos_por_tipo.plot(kind='bar', figsize=(12, 6))
plt.title('Média de Atributos Principais por Tipo de Criatura')
plt.xlabel('Tipo de Criatura')
plt.ylabel('Média')
plt.xticks(rotation=0)
plt.legend(title='Atributo Principal', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


'CORRELAÇÃO ENTRE ATRIBUTOS'
import seaborn as sns
# Suponha que você tenha um DataFrame chamado 'df_dd' com os atributos principais
atributos_principais = ['str', 'dex', 'con', 'int', 'wis', 'cha']
# Calcular a matriz de correlação
correlacao_atributos = df_dd[atributos_principais].corr()
# Plotar um mapa de calor da matriz de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(correlacao_atributos, annot=True, cmap='coolwarm', linewidths=1)
plt.title('Matriz de Correlação entre Atributos Principais')
plt.show()
print(correlacao_atributos)
"A correlação entre str (força) e os outros atributos é a seguinte:Com dex (destreza), a correlação é -0.192704, o que indica uma correlação negativa fraca. Isso significa que, em geral, criaturas mais fortes tendem a ser menos ágeis, mas a relação não é forte."
'Com "con" (constituição), a correlação é 0.837820, o que indica uma correlação positiva forte. Isso significa que criaturas mais fortes também tendem a ter maior constituição.'
'Com "int" (inteligência), a correlação é 0.345380, o que indica uma correlação positiva moderada. Criaturas mais fortes têm uma tendência a ter uma inteligência um pouco maior, mas a relação não é tão forte quanto com a constituição.'








'Alinhamento e cr(classe de dificuldade)'
import re
def converter_fracao_em_decimal(fracao):
    partes = re.findall(r'\d+', fracao)
    if len(partes) == 2:
        numerador, denominador = map(int, partes)
        return numerador / denominador
    elif len(partes) == 1:
        return int(partes[0])
    else:
        return None
# Converter valores da coluna 'cr' em números decimais
df_dd['cr'] = df_dd['cr'].apply(converter_fracao_em_decimal)
# Função para agrupar criaturas em "más" e "não más"
def agrupar_alinhamento(alinhamento):
    if alinhamento in ['lawful evil', 'chaotic evil', 'neutral evil', 'any non-good alignment', 'any evil alignment']:
        return 'más'
    else:
        return 'não más'
# Criar uma coluna 'grupo_alinhamento' com o agrupamento
df_dd['grupo_alinhamento'] = df_dd['align'].apply(agrupar_alinhamento)
# Criar DataFrames separados para criaturas "más" e "não más"
criaturas_más = df_dd[df_dd['grupo_alinhamento'] == 'más']
criaturas_não_más = df_dd[df_dd['grupo_alinhamento'] == 'não más']
# Calcular a média do CR para criaturas "más" e "não más"
media_cr_más = criaturas_más['cr'].mean()
media_cr_não_más = criaturas_não_más['cr'].mean()
# Exibir as médias
print("\n\n\n\nMédia do CR das criaturas 'más':", media_cr_más)
print("Média do CR das criaturas 'não más':", media_cr_não_más)

#GRAFICO SE PRECISAR
"""# Dados das médias de CR para alinhamentos maus e não maus
medias_cr_alinhamentos = [media_cr_más, media_cr_não_más]
# Rótulos para as barras
rótulos_alinhamentos = ['Maus', 'Não Maus']
# Cores das barras
cores = ['#FF0000', '#0000FF']
# Cria o gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(rótulos_alinhamentos, medias_cr_alinhamentos, color=cores)
plt.title('Média das Classes de Dificuldade (CR) para Alinhamentos Maus e Não Maus')
plt.xlabel('Alinhamento')
plt.ylabel('Média de CR')
# Exibe o gráfico
plt.show()"""






