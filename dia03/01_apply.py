# %%
import pandas as pd

# %%

df_produto = pd.read_csv("../data/produto.csv")
df_produto
# %%

df_produto["descItem"].unique()
# %%

## maneira 1
## criando a nossa propria funcao def
def is_massa(x):
    return x.lower().startswith('massa')

filtro_massa = df_produto["descItem"].apply(is_massa)

df_produto[filtro_massa]


# %%
df_produto["flMassa"] = df_produto["descItem"].apply(is_massa)

df_produto[df_produto["flMassa"]]
# %%

# função anonima (lambida) quando vai usar apenas em um local e é simples uma linha

# maneira 2
nova_is_massa = lambda linha: linha.lower().startswith('massa')
df_produto["descItem"].apply(nova_is_massa)

# %%

# maneira 3
## usando função anonima apply

df_produto["descItem"].apply(lambda linha: linha.lower().startswith('massa'))
# %%

## maneira 4
## usando o método de str
df_produto["descItem"].str.lower().str.startswith("massa")


# %%
