# %%

import pandas as pd
# %%
df = pd.read_csv("../data/pedido.csv")
df
# %%

filtro_uf = df["descUF"] == 'São Paulo'

df[filtro_uf]
# %%

# É de SP e pediu ketchup
filtro_sp_ketchup = (df["descUF"] == 'São Paulo') & (df["flKetchup"])
df[filtro_sp_ketchup] 
# %%

# maneira 1
filtro_ufs_ketchup = ((df["descUF"] == 'São Paulo') | (df["descUF"] == 'Rio de Janeiro' )| (df["descUF"] == 'Paraná' )) & (df["flKetchup"])
# df[filtro_uds_ketchup]["descUF"].unique()
df[filtro_ufs_ketchup]
# %%

# maneira 2
uf_recortes = ['São Paulo', 'Rio de Janeiro', 'Paraná']
filtro_ufs_ketchup = df["descUF"].isin(uf_recortes) & df["flKetchup"]
df[filtro_ufs_ketchup]

# %%

# pedidos que não deixaram recado
filtro_txt_na = df["txtRecado"].isna()
df[filtro_txt_na]

# %%
