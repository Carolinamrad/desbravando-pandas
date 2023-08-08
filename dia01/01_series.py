# %%
import pandas as pd

# %%

# Isso é uma lista
idade = [31, 23, 33, 2, 60, 51, 45, 17, 56, 28]

# Busca valor de um indice determinado
idade[0]

# %%

s_idade = pd.Series(idade)
s_idade

# %%

# Métodos das séries 
media = s_idade.mean()
variancia = s_idade.var()
desv_pad = s_idade.std()
describe = s_idade.describe()

describe
# %%

nova_idade = []
for i in idade:
    if i >= 30:
        nova_idade.append(i)

nova_idade
# %%
filtro = s_idade >= 30

s_idade[filtro]
# s_idade[~filtro] o ~é a negativa do filtro

# %%
