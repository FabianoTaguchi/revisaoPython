# Crie um código em Python que verifique se o saldo que você possui é suficiente para realizar uma compra. Se for, subtraia o valor da compra do saldo e imprima o novo saldo formatado. Se não, imprima uma mensagem de saldo insuficiente.

saldo = float(input("Qual valor do seu saldo? "))
valorCompra = float(input("Informe o valor da compra: "))

if saldo >= valorCompra:
    saldo -= valorCompra
    print(f"Compra realizada com sucesso. Seu novo saldo é R$ {saldo:.2f}.")
else:
    print("Saldo insuficiente para realizar a compra.")