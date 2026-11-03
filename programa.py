from funcoes import *

frota = {}

navios = [
    ['porta-aviões', 4, 1],
    ['navio-tanque', 3, 2],
    ['contratorpedeiro', 2, 3],
    ['submarino', 1, 4],
]

for nome, tamanho, quantidade in navios:
    for i in range(quantidade):
        valida = False
        while not valida:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if nome == 'submarino':
                orientacao = 'horizontal'
            else:
                opcao = int(input('[1] Vertical [2] Horizontal >'))
                if opcao == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if not valida:
                print('Esta posição não está válida!')

        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)

print(frota)