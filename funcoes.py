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
