# Crie uma lista que receba valores de produtos. Use um laço de repetição para percorrer a lista e somar todos os valores. Imprima o valor total com formatação de duas casas decimais.

precos = []
somaTotal = 0

continuar = "S"

while continuar.upper() == "S":
    preco = float(input("Informe o valor do produto: "))
    precos.append(preco)
    somaTotal += preco
    
    continuar = input("Deseja informar outro valor? (S/N): ")

print(f"O valor total dos produtos é: R${somaTotal:.2f}")
