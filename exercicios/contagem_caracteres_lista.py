def contar_caracteres(s):
    """Função que conta caracteres de uma string
    ex:

    >>> contar_caracteres('paulo')
    a: 1
    l: 1
    o: 1
    p: 1
    u: 1
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada
    """
    caractere_ordenado = sorted(s)
    caractere_anterior =  caractere_ordenado[0]
    contagem = 1

    for caractere in caractere_ordenado[1:]:
        if caractere == caractere_anterior:
            contagem += 1
        else:
            print(f'{caractere_anterior}: {contagem}')
            caractere_anterior = caractere
            contagem = 1

    print(f'{caractere_anterior}: {contagem}')


if __name__ == '__main__':
    contar_caracteres('paulo')
    print()
    contar_caracteres('banana')
