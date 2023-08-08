# %%
import pandas as pd

#%%

# o .. é para subir um nivel da parta onde estou no momento
df = pd.read_csv("../data/pedido.csv")
df
# %%

# atributos do DF
df.columns
# %%

# quantidade de linhas e colunas
df.shape
# %%

df.index
# %%

# quanto ocupa em memória
df.info(memory_usage="deep")
# %%

# mostra os indices e os valores de cada coluna
df.dtypes
# %%

df.head(10)

# %%

df.tail(10)
# %%
# Dados aleatórios
df.sample(10)

# %%
