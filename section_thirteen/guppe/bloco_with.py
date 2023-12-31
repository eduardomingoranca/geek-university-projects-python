"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with eh utilizado para criar um contexto de trabalho onde os recursos
utilizados sao fechados apos o bloco with.

arquivo = open('texto.txt')

"""

# O block with - Forma Pythonica de manipular arquivos

with open('files/texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)


# print(arquivo.read())

print(arquivo.closed)
