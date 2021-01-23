"Esta lina é chamada de DOCSTRING e aparece no console quando importado (from from matematica.base import mat) e chamado o help(mat)"
def soma(parcela, parcela_2):
    """Esta função calcula a soma de duas parcelas
    :param parcela: number
    :param parcela_2: number
    :return: number
    """
    return parcela + parcela_2


# a linha abaixo verifica se o arquivo está sendo executado direto, não por chamada
# a expressão __name__ é chamado de DANDER name
if __name__ == '__main__':
    print(soma(1, 2))
