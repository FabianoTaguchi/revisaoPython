# Crie um programa que declare três variáveis com valores numéricos referente a notas de alunos. Calcule a média dessas notas e, usando uma estrutura de condição, verifique se o aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"O aluno foi aprovado com média {media:.2f}.")
else:
    print(f"O aluno foi reprovado com média {media:.2f}.")