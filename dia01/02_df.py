# %%
import pandas as pd
# %%

# Dicionário
data = {
    "nome":["Teo", "Nah", "Maria", "João", "Jessica", "Carol"],
    "idade":[30, 33, 2, 45, 65, 40],
    "cor":["Preto", "Verde", "Azul", "Vermelho", "Amarelo", "Rosa"],
    "renda":[3550, 3000, 1000, 5000, 4500, 6222]
}
data["idade"]

# %%
# DataFrame é um agregador de series
df = pd.DataFrame(data)
df["idade"]
# %%

# df[["idade", "renda"]].mean()
df.describe
# %%
