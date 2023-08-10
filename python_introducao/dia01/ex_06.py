# Faça um programa que receba um número em segundos, converta esse número em horas

# %%

segundos = int(input("Entre com o tempo em segundos: "))

horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)

minutos = segundos // 60
segundos = segundos % 60

print(f"{horas:02}:{minutos:02}:{segundos:02}")
# %%
