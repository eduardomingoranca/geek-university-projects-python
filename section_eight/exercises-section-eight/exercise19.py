"""
Faca uma funcao que retorne o maior fator primo de um numero
"""
import math


def maior_primo(n):
    # Fazemos um loop para percorrer os numeros de 2 ate o valor digitado
    i = 2
    maior = []
    while i <= n:
        # Fazemos um casting para que nos retorne um numero inteiro
        raiz = int(math.sqrt(i))
        primo = 0

        # Fazemos outro loop para contar os divisiveis
        j = raiz
        while j > 1:
            # Se o numero for divisivel, aumentamos o contador
            if i % j == 0:
                # Aumentamos o contador
                primo = primo + 1
            j = j - 1

        # Dependendo do numero de divisiveis sabemos se eh primo ou nao,
        # se for primo o contador sera 0
        if primo < 1:
            maior.append(i)
        i = i + 1

    return max(maior)


try:
    loop = True
    while loop:
        numero = int(input('Informe um numero inteiro: '))

        if numero > 1:
            loop = False
            print(f'MAIOR FATOR PRIMO: {maior_primo(numero)}')

except ValueError:
    print('FORMATO INVALIDO!')
