# %%
import pandas as pd

# %%

df_produto = pd.read_csv("../data/produto.csv")
df_produto["primeiroNome"] = df_produto["descItem"].apply(lambda x: x.lower().split(" ")[0])
df_produto

# %%

df_produto = df_produto.sort_values(
        by=["vlPreco", "descItem"],
        ascending=[False, True]
)
df_produto

df_produto.drop_duplicates(subset=["primeiroNome", "vlPreco"], keep="first")
# %%

df_pedido = pd.read_csv("../data/pedido.csv")
# se uma celula/coluna tiver na toda a linha será removida

df_pedido.dropna()
# %%

# se alguma for nula já deleta
df_pedido.dropna(how="any")

# se todas forem nula já deleta
df_pedido.dropna(how="all")

# %%

df_pedido.dropna(subset=["txtRecado", "flKetchup"],
                         how="any")


# %%
