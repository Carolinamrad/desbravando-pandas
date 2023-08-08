# %%
import pandas as pd

# %%

df = pd.read_csv("../data/pedido.csv")
df
# %%

df.head()
# %%


colunas = ['idPedido', 'flKetchup']
df[colunas]
# %%
# essa opção é igual a de cima
df[['idPedido', 'flKetchup']]

# %%
df.head()

# %%

# caso queira alterar a ordem das colunas 
colunas = [
        'idPedido', 
        'descUF', 
        'flKetchup', 
        'txtRecado', 
        'dtPedido']

# Altera a order das colunas de fato o dataframe
df = df[colunas]

df
# %%

# navegando em linhas

# cria um novo dataframe novo com 100 registros aleatórios do primeiro 
df_sample = df.sample(100)
# %%

# iloc (integer location) busca o registro na posição e não no índice
df_sample.iloc[0]

# %%
# faixa de linhas
df_sample.iloc[0:4]

# %%
# lista de linhas
df_sample.iloc[0,2,4,13]

# %%

# busca o indice
df.loc[33:384]

# %%

df_sample.iloc[0:10][['idPedido', 'dtPedido']]

# %%
