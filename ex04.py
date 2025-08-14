# Crie um programa que declare um número com um valor inteiro. Use uma estrutura de condição if-elif-else para classificar o número nas seguintes categorias e imprimir a mensagem correspondente:
# Positivo (maior que 0)
# Negativo (menor que 0)
# Zero (igual a 0)


numero = int(input("Informe um número: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print("O número é zero.")