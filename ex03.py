# Crie um programa que leia o valor de um produto para compra e o percentual do desconto. Calcule o valor do desconto e o valor final do produto.


valor = float(input("Qual o valor do produto? "))
desconto = float(input("Informe o percentual do desconto: "))

desconto = valor * (desconto / 100)
valorPagar = valor - desconto

print(f"O valor do produto é R$ {valor:.2f}.")
print(f"O desconto aplicado é de R$ {desconto:.2f}.")
print(f"O valor fivalorPagar a ser pago é R$ {valorPagar:.2f}.")