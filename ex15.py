precos = []
somaTotal = 0

for i in range(4):
    preco = float(input(f"Informe o valor do produto {i+1}: "))
    precos.append(preco)
    somaTotal += preco

print(f"O valor total dos produtos é: R${somaTotal:.2f}")
