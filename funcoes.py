def define_posicoes (linha,coluna, orientacao, tamanho):
    lista = []
    for i in range(tamanho):
        if orientacao == "horizontal":
            coluna_atual = coluna + i
            mini_lista = [linha, coluna_atual]
            lista.append(mini_lista)
        
        elif orientacao == "vertical":
            linha_atual = linha + i
            mini_lista = [linha_atual, coluna]
            lista.append(mini_lista)
        
    return lista

def preenche_frota (frota, nome, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome in frota:
        frota[nome].append(posicoes)
    else:
        frota[nome] = [posicoes]
    return frota

def faz_jogada (tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0] * 10)

    for nome in frota:
        for embarcacao in frota[nome]:
            for posicao in embarcacao:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    total = 0
    for navios in frota.values():
        for navio in navios:
            afundou = True
            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
            if afundou:
                total += 1
    return total

def define_posicoes (linha,coluna, orientacao, tamanho):
    lista = []
    for i in range(tamanho):
        if orientacao == "horizontal":
            coluna_atual = coluna + i
            mini_lista = [linha, coluna_atual]
            lista.append(mini_lista)
        
        elif orientacao == "vertical":
            linha_atual = linha + i
            mini_lista = [linha_atual, coluna]
            lista.append(mini_lista)
        
    return lista


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas = define_posicoes(linha, coluna, orientacao, tamanho)

    for l, c in novas:
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False

    for navios in frota.values():
        for navio in navios:
            for posicao in navio:
                if posicao in novas:
                    return False

    return True
