# Escreva um programa que receba o raio de uma circunferencia em cm
# Retornar a área e o perimetro

# %%

raio = float(input("Informe o valor do raio da circunferência em cm: "))
pi = 3.14

area = pi * (raio ** 2)
perimetro = 2 * pi * raio

print("Área: ", round(area,2), sep="")
print("Perímetro: ", round(perimetro,2), sep="")

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
# %%
