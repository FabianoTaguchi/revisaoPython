# Crie uma variável de string com a frase "Python é uma linguagem poderosa". Use métodos de string para:
# Imprimir a frase em letras maiúsculas.
# Substituir a palavra "poderosa" por "incrível".
# Verificar se a frase começa com a palavra "Python".

frase = "Python é uma linguagem poderosa"

print(f"Frase em maiúsculas: {frase.upper()}")
print(f"Frase alterada: {frase.replace('poderosa', 'incrível')}")
if frase.startswith('Python')==True:
    print(f"A frase começa com Python")
else:
    print(f"A frase não começa com Python")
