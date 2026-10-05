# This is the Python script for your project
#ProjetoFp
def eh_tabuleiro(arg):
    '''eh_tabuleiro(arg) vai receber um argumento e verifica se o argumento eh um tabuleiro,
    caso seja um tabuleiro devolve True, se nao for devolve False.
        Input: arg
        Output(caso seja tabuleiro): True
        Output(caso nao seja tabuleiro): False'''
    if type(arg) != tuple or len(arg) == 0 or type(arg[0]) != tuple:
        return False
    if len(arg) < 2 or len(arg) > 100:
        return False
    if len(arg[0]) < 2 or len(arg[0]) > 100:
        return False
    for linhas in arg:
        if type(linhas) != tuple or len(linhas) != len(arg[0]):
            return False
        for valor in linhas:
            if type(valor) != int or valor not in (-1, 0, 1):
                return False
    return True


def eh_posicao(arg):
    '''eh_posicao(arg) vai receber um argumento e vai verificar se eh uma posicao,
    caso seja uma posicao devolve True, se nao for devolve False.
        Input: arg
        Output(caso seja posicao): True
        Output(caso nao seja posicao): False'''
    if type(arg) != int:
          return False
    elif arg < 1  or arg > 10000:
          return False
    return True

def obtem_dimensao(tab):
    '''obtem_dimensao(tab) vai receber um tabuleiro e devolve a dimensao do tabuleiro,
    dado por 2 interios, m = numero de linhas e n = numero de colunas.
        Input: tab
        Output: dimensao = (m, n)'''
    m = len(tab) 
    n = len(tab[0])
    dimensao = (m, n)
    return dimensao

def tab_um_tuplo(tab):
    '''tap_um_tuplo(tab) eh uma funcao de suporte,
    que recebe um tabuleiro e devolve um tuplo onde estao todos os valores do tabuleiro,
    sem a divisao por linhas.
        Input: tab
        Output: tap_tuplo_unico'''
    tab_tuplo_unico = ()
    for linhas in tab:
        for valor_posicao in linhas:
            tab_tuplo_unico += (valor_posicao,)
    return tab_tuplo_unico

def obtem_valor(tab, pos):
    '''obtem_valor(tab, pos) eh uma funcao que vai receber um tabuleiro e uma posicao
    e vai devolver um inteiro, que corresponde,
    ao valor que dada posicao tem dentro do tabuleiro.
        Input: tab, pos
        Output: valor'''
    (tap_tuplo_unico) = tab_um_tuplo(tab)
    for indice, valor in enumerate(tap_tuplo_unico):
        if indice + 1 == pos:
            return valor


def obtem_coluna(tab, pos):
    '''obtem_coluna(tab, pos) recebe um tabuleiro e uma posicao
    e com o auxilio da funcao obtem_dimensao(tab), devolve um tuplo com todas as posicoes,
    que se encontram na mesma coluna que dada posicao, ordenadas de menor para maior.
        Input: tab, pos
        Output: coluna'''
    (m, n) = obtem_dimensao(tab)
    coluna = ()
    copia_pos = pos
    while copia_pos > n:
        copia_pos = copia_pos - n  
    for num_linhas in range(m):
        coluna += (num_linhas*n + copia_pos,) 
    return coluna

def obtem_linha(tab, pos):
    '''obtem_linha(tab, pos) recebe um tabuleiro e uma posicao
    e com o auxilio da funcao obtem_dimensao(tab), devolve um tuplo com todas as posicoes,
    que se encontram na mesma linha que dada posicao, ordenadas de menor para maior.
        Input: tab, pos
        Output: linha'''
    (_,n) = obtem_dimensao(tab)
    linha = ()
    num_linha = (pos-1) // n
    inicio_linha = num_linha * n + 1
    for posicao in range(inicio_linha, inicio_linha + n):
        linha += (posicao,)
    return linha

def obtem_diagonais(tab, pos):
    '''obtem_diagonais(tab, pos) recebe um tabuleiro e uma posicao
    e com o auxilio da funcao obtem_dimensao(tab), devolve um tuplo,
    com outros dois tuplos, diagonal descendente e diagonal ascendente, respetivamente.
    A diagonal descendente vai ser um tuplo com todas as posicoes na diagonal,
    da esquerda para a direita, ordenados do menor para o maior.
    A diagonal ascendente vai ser um tuplo com todas as posicoes na anti-diagonal ascendente,
    da esquerda para a direita, estando assim ordenados do maior para o menor.
        Input: tab, pos
        Output: diagonal_descendente, diagonal_ascendente'''
    (m,n) = obtem_dimensao(tab)
    ultima_posicao = m*n
    limite_superior = obtem_linha(tab, 1)
    limite_inferior = obtem_linha(tab, ultima_posicao)
    limite_lateral_esq = obtem_coluna(tab, 1)
    limite_lateral_dir = obtem_coluna(tab, n)
    limites = set(limite_superior + limite_inferior + limite_lateral_esq + limite_lateral_dir)
    diagonal_descendente = (pos,)
    diagonal_ascendente = (pos,)
    
    passo_descendente = n + 1
    if pos not in limite_lateral_esq + limite_superior:
        contandor_desc_asc = pos
        while contandor_desc_asc - passo_descendente > 0 and (contandor_desc_asc not in limites or contandor_desc_asc == pos):
            contandor_desc_asc -= passo_descendente
            diagonal_descendente = (contandor_desc_asc,) + diagonal_descendente
    
    if pos not in limite_lateral_dir + limite_inferior or pos == 1:
        contandor_desc_dsc = pos
        while contandor_desc_dsc + passo_descendente <= ultima_posicao and (contandor_desc_dsc not in limites or contandor_desc_dsc == pos):
            contandor_desc_dsc += passo_descendente
            diagonal_descendente = diagonal_descendente + (contandor_desc_dsc,)

        
    passo_ascendente = n - 1
    if pos not in limite_lateral_esq + limite_inferior:
        contandor_ascd_dsc = pos
        while contandor_ascd_dsc + passo_ascendente <= ultima_posicao and (contandor_ascd_dsc not in limites or contandor_ascd_dsc == pos):
            contandor_ascd_dsc += passo_ascendente
            diagonal_ascendente = (contandor_ascd_dsc,) + diagonal_ascendente

    if pos not in limite_lateral_dir + limite_superior:
        contandor_ascd_asc = pos
        while contandor_ascd_asc - passo_ascendente > 0 and (contandor_ascd_asc not in limites or contandor_ascd_asc == pos):
            contandor_ascd_asc -= passo_ascendente
            diagonal_ascendente = diagonal_ascendente + (contandor_ascd_asc,)

    return diagonal_descendente, diagonal_ascendente



def tabuleiro_para_str(tab):
    '''tabuleiro_para_str(tab) recebe um tabuleiro e devolve uma cadeia de caracteres,
    que representa a visualizacao do tabuleiro, usando "X", para pecas pretas,
    "O", para pecas brancas, e "+", para posicoes livres.
        Input: tab
        Output: tabuleiro'''
    tabuleiro = ""
    linhas_index= len(tab) -1
    colunas = len(tab[0])
    for index, linhas in enumerate(tab):
        ja_passou = False
        for posicao in linhas:
            if ja_passou == False:
                if posicao == 0: 
                    tabuleiro += "+"
                elif posicao == 1:
                    tabuleiro += "X"
                else:
                    tabuleiro += "O"
                ja_passou = True
            else:
                if posicao == 0: 
                    tabuleiro += "---+"
                elif posicao == 1:
                    tabuleiro += "---X"
                else:
                    tabuleiro += "---O"
        if index != linhas_index:
            tabuleiro += ("\n" + ("|   ") * (colunas-1) + "|\n")

    return tabuleiro
    

def eh_posicao_valida(tab, pos):
    '''eh_posicao_valida(tab, pos) vai receber um tabulerio e uma posicao, e vai verificar se
    dada posicao existe no tabuleiro, caso exista retorna True, caso contrario retorna False.
    Ao mesmo tempo usa outras funcoes para verificar os argumentos, levantando um erro caso
    algum seja invalido.
        Input: tab, pos
        Output(caso seja uma posicao valida): True
        Output(caso nao seja uma posicao valida): False'''
    (m,n) = obtem_dimensao(tab)
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError("eh_posicao_valida: argumentos invalidos")
    if pos in range(1, m*n+1):
        return True
    else:
        return False


def eh_posicao_livre(tab, pos):
    '''eh_posicao_livre(tab,pos) vai receber um tabulerio e uma posicao, e vai verificar se
    dada posicao eh igual a 0 no tabuleiro, ou seja, que esta livre,
    caso seja retorna True, caso contrario retorna False.
    Ao mesmo tempo usa outras funcoes para verificar os argumentos, levantando um erro caso
    algum seja invalido.
        Input: tab, pos
        Output(caso exita uma posicao livre): True
        Output(caso nao exista uma posicao livre): False'''
    (tab_tuplo_unico) = tab_um_tuplo(tab)
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    for posicoes, valor_posicao in enumerate(tab_tuplo_unico):
        if posicoes == pos-1:
            if valor_posicao == 0:
                return True
            if valor_posicao == -1:
                return False
            if valor_posicao == 1:
                return False
    
        
def obtem_posicoes_livres(tab):
    '''obtem_posicoes_livres(tab) recebe um tabuleiro e vai devolver um tuplo,
    contendo todas as posicoes livres do tabuleiro, ordenadas de menor para maior.
    Ao mesmo tempo usa outra funcao para verificar o argumento, levantando um erro caso
    seja invalido.
        Input: tab
        Output: posicoes_livres'''
    (m,n) = obtem_dimensao(tab)
    posicoes_livres = ()
    if not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    for pos in range(1, m*n+1):
        if  eh_posicao_livre(tab, pos):
            posicoes_livres += (pos,)
    return posicoes_livres

        
def obtem_posicoes_jogador(tab, jog):
    '''obtem_posicoes_livres(tab) recebe um tabuleiro e um inteiro(jog) e vai devolver um tuplo,
    contendo todas as posicoes do tabuleiro onde se encontra esse inteiro, ordenadas de menor para maior.
    Ao mesmo tempo usa outra funcao e condicoes para verificar os argumentos, levantando um erro caso
    algum seja invalido.
        Input: tab
        Output: pos_jogador'''
    pos_jogador = ()
    tab_unico = tab_um_tuplo(tab)
    if not eh_tabuleiro(tab) or type(jog) != int or jog not in (-1, 1):
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")
    for pos, coluna in enumerate(tab_unico):
        if coluna == jog:
            pos_jogador += (pos + 1,)
    return pos_jogador


def obtem_posicoes_adjacentes(tab, pos):
    '''obtem_posicoes_adjacentes(tab, pos) recebe um tabuleiro e uma posicao e devolve um tuplo,
    contendo todas as posicoes adjacentes(distancia de 1 para a posicao), ordenadas do menor para o maior.
    Ao mesmo tempo usa outras funcoes para verificar os argumentos, levantando um erro caso
    algum seja invalido.
        Input: tab, pos
        Output: posicoes_adjacentes_ordenadas
    '''

    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    
    (m, n) = obtem_dimensao(tab)
    posicoes_adjacentes = ()
    posicoes_adjacentes_ordenadas = ()
    num_linha = (pos - 1) // n
    num_coluna = (pos - 1) % n
    
    for linha in range(num_linha - 1, num_linha + 2):
        for coluna in range(num_coluna - 1, num_coluna + 2):
            if (linha != num_linha) or (coluna != num_coluna):
                if 0 <= linha < m and 0 <= coluna < n:
                    adjacente = linha * n + coluna + 1
                    posicoes_adjacentes += (adjacente,)

    for ordem in range(1, m * n + 1):
        if ordem in posicoes_adjacentes:
            posicoes_adjacentes_ordenadas += (ordem,)

    return posicoes_adjacentes_ordenadas

def ordena_posicoes_tabuleiro(tab, tup):
    '''ordena_posicoes_tabuleiro(tab, tup) recebe um tabuleiro e um tuplo que contem um numero de posicoes,
    tuplo pode ser vazio, e devolve um tuplo com posicoes ordenadas, do menor para o maior, de acordo com a
    distancia ao centro, as posicoes com iguais distancias ao centro sao ordenadas de forma ascendente,
    de acordo com a posicao que ocupam no tabuleiro.
    Ao mesmo tempo usa outra funcao e condicoes para verificar os argumentos, levantando um erro caso
    algum seja invalido.
        Input: tab
        Output: posicoes_ordenadas'''
    (m, n) = obtem_dimensao(tab)
    centro = (m // 2) * n + (n // 2) + 1
    centro_d2 = (((centro-1)//n),((centro-1) % n)) 
    posicoes_ordenadas = ()
    pos_distancia = ()
    if not eh_tabuleiro(tab) or type(tup) != tuple:
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    for pos in tup:
        if not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or type(pos) != int:
          raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
        if pos in range(1, m*n+1):
            pos_d2 = (((pos-1)//n),((pos-1) % n))
            distancia = max(abs(centro_d2[0]- pos_d2[0]), abs(centro_d2[1]-pos_d2[1]))
            pos_distancia += ((distancia, pos),)

    pos_distancia = tuple(sorted(pos_distancia))
    for indice in range(len(pos_distancia)):
        posicao = pos_distancia[indice][1]
        posicoes_ordenadas += (posicao,)

    return posicoes_ordenadas

def marca_posicao(tab, pos, jog):
    '''marca_posicao(tab, pos, jog) recebe um tabuleiro, uma posicao e um inteiro(jog),
    e devolve um tabuleiro igual ao tabuleiro de imput, porem o valor na posicao dada eh
    substituido pelo valor do jog.
    Ao mesmo tempo usa outras funcoes e condicoes para verificar os argumentos, levantando um erro caso
    algum seja invalido.
        Input: tab, pos, jog
        Output: tab_jog'''
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or not eh_posicao_livre(tab, pos) or type(jog) != int or jog not in (-1,1):
        raise ValueError("marca_posicao: argumentos invalidos")
    (_,n) = obtem_dimensao(tab)
    tab_jog = ()
    for indice_linha, linhas in enumerate(tab):
        linha_nova = ()
        for indice, valores in enumerate(linhas):
            if pos == n * (indice_linha) + indice+1:
                linha_nova += (jog,)
            else:
                linha_nova += (valores,)
        tab_jog += (linha_nova,)
    
        
    return tab_jog


def verifica_k_linhas(tab, pos, jog, k):
    '''verifica_k_linhas(tab, pos, jog, k) recebe um tabuleiro, uma posicao, 1 inteiro(jog) e um intero positivo(k).
    Verifica se o jogador tem k pecas consecutivas em qualquer direcao (horizontal, vertical ou diagonal)
    a partir da posicao fornecida. Devolve True se o jogador tiver pelo menos k pecas consecutivas; caso
    contrario, devolve False.
    Ao mesmo tempo usa outras funcoes e condicoes para verificar os argumentos, levantando um erro caso
    algum seja invalido.
        Input: tab, pos, jog, k
        Output (caso tenha k pecas consecutivas): True
        Output (caso nao tenha k pecas consecutivas): False'''
    (coluna_pos) = obtem_coluna(tab, pos)
    (linha_pos) = obtem_linha(tab, pos)
    (diagonais_pos) = obtem_diagonais(tab, pos)
    contador = 0
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or type(jog) != int or jog not in (-1,1) or type(k) != int or not k > 0 or not eh_posicao_valida(tab, pos):
        raise ValueError("verifica_k_linhas: argumentos invalidos")
    
    if obtem_valor(tab, pos) != jog:
        return False
        
    for direcao in (coluna_pos, linha_pos, diagonais_pos[0],diagonais_pos[1]):
        contador = 0
        for posicao in direcao:
            if obtem_valor(tab, posicao) == jog:
                contador += 1
                if contador >= k:
                    return True
            else:
                contador = 0

    return False

def eh_fim_jogo(tab, k):
    '''eh_fim_jogo(tab, k) recebe um tabuleiro e um inteiro positivo(k) e verifica se o jogo terminou.
    O jogo termina se houver k pecas consecutivas de um jogador em qualquer direcao ou
    se nao houver mais posicoes livres no tabuleiro. Devolve True se o jogo terminou;
    caso contrario, devolve False.
    Ao mesmo tempo usa outras funcoes e condicoes para verificar os argumentos, levantando um erro caso
    algum seja invalido.
        Input: tab, k
        Output (caso o jogo tenha terminado): True
        Output (caso o jogo nao tenha terminado): False'''
    (m, n) = obtem_dimensao(tab)
    
    if not eh_tabuleiro(tab) or (type(k) != int) or not k > 0:
        raise ValueError("eh_fim_jogo: argumentos invalidos")

    for jog in (1, -1):
        for pos in range(1, m * n + 1):
            if verifica_k_linhas(tab, pos, jog, k):
                return True
    
    if len(obtem_posicoes_livres(tab)) == 0:
        return True

    return False
 

def escolhe_posicao_manual(tab):
    '''escolhe_posicao_manual(tab) permite ao usuario escolher manualmente uma posicao no tabuleiro.
    Recebe um tabuleiro como argumento e devolve a posicao escolhida pelo usuario. Valida a posicao
    para garantir que eh uma posicao livre e valida no tabuleiro.
    Ao mesmo tempo usa outra funcao para verificar os argumento, levantando um erro caso seja invalido.
        Input: tab
        Output: posicao escolhida'''
    if not eh_tabuleiro(tab):
        raise ValueError("escolhe_posicao_manual: argumento invalido")
    pos = -1
    while not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or not eh_posicao_livre(tab, pos):
        pos = (input("Turno do jogador. Escolha uma posicao livre: "))
        if pos.isdigit():
            pos = int(pos)
    
    return pos

def modo_facil(tab, jog):
    '''modo_facil(tab, jog) eh uma funcao que vai agir na funcao escolhe_posicao_auto,
    que recebe um tabuleiro, um inteiro(jog) e um inteiro positivo(k), e devolve a posicao a jogar
    com base nas seguintes regras:
    "Se existir no tabuleiro pelo menos uma posicao livre e adjacente a uma pedra
    propria, jogar numa dessas posicoes;
    Se nao, jogar numa posicao livre."
        Input: tab, jog
        Output: posicao a jogar
    '''
    posicoes_jogador = ordena_posicoes_tabuleiro(tab, obtem_posicoes_jogador(tab, jog))
    for pos_jog in posicoes_jogador:
        posicoes_adjacentes = ordena_posicoes_tabuleiro(tab, obtem_posicoes_adjacentes(tab, pos_jog))
        for pos_adj in posicoes_adjacentes:
            if eh_posicao_livre(tab, pos_adj):
                return pos_adj
    return ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))[0]


def modo_normal(tab, jog, k):
    '''modo_normal(tab, jog, k) eh uma funcao que vai agir na funcao escolhe_posicao_auto,
    que recebe um tabuleiro, um inteiro(jog) e um inteiro positivo(k), e devolve a posicao a jogar
    com base nas seguintes regras:
    "Determinar o maior valor de L ≤ k tal que o proprio ou o adversario podem
    conseguir colocar L pecas consecutivas na proxima jogada numa linha vertical,
    horizontal ou diagonal que contenha essa jogada. Para esse valor:
    Se existir pelo menos uma posicao que permita obter uma linha que contenha
    essa posicao com L pedras consecutivas proprias, jogar numa dessas posicoes;
    Se nao, jogar numa posicao que impossibilite o adversario de obter L pedras
    consecutivas numa linha que contenha essa posicao."
        Input: tab, jog, k
        Output: posicao a jogar
    '''
    L_jog = 0
    L_bot = 0
    L_max = 0
    posicoes_jogar = ()
    posicoes_block = ()
    
    for pos in ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab)):
        copia_k = k
        while copia_k != 0:
            if verifica_k_linhas(marca_posicao(tab, pos, jog), pos, jog, copia_k):
                L_jog = copia_k
                break
            else:
                copia_k -= 1

        copia_k = k
        while copia_k != 0:
            if verifica_k_linhas(marca_posicao(tab, pos, -jog), pos, -jog, copia_k):
                L_bot = copia_k
                break
            else:
                copia_k -= 1

        if L_jog > L_max or L_bot > L_max:
            L_max = max(L_jog, L_bot)
            if L_max == L_jog:
                posicoes_jogar = (pos,)
                posicoes_block = ()
            else:
                posicoes_block = (pos,)
                posicoes_jogar = ()

        elif L_max == max(L_bot, L_jog):
            if L_max == L_jog:
                posicoes_jogar += (pos,)
            else:
                posicoes_block += (pos,)
    
    if posicoes_jogar:
        return ordena_posicoes_tabuleiro(tab, posicoes_jogar)[0]
    else:
        return ordena_posicoes_tabuleiro(tab, posicoes_block)[0]
    
def tab_simulacao(tab, pos, jog, k):
    '''tab_simulacao(tab, pos, jog, k) eh uma funcao que vai agir na funcao modo_dificil,
    com o objetivo de criar cada uma das simulacoes dos jogos, recebe um tabuleiro, uma posicao,
    um inteiro(jog) e um inteiro positivo(k), e devolve um tabuleiro simulado do jogo inteiro, comecando
    em cada posicao, com as regras do modo_normal.
        Input: tab, pos, jog, k
        Output: tab_simulado'''
    tab_simulado = marca_posicao(tab, pos, jog)
    jog_atual = -jog

    while not eh_fim_jogo(tab_simulado, k):
        prox_pos = modo_normal(tab_simulado, jog_atual, k)
        tab_simulado = marca_posicao(tab_simulado, prox_pos, jog_atual)
        jog_atual = -jog_atual
        for jogador in (-1, 1):
            if verifica_k_linhas(tab_simulado, prox_pos, jogador, k):
                return(True, jogador)
            
    return(False, 0)
    
    
    


def modo_dificil(tab, jog, k):
    '''modo_normal(tab, jog, k) eh uma funcao que vai agir na funcao escolhe_posicao_auto, 
    que recebe um tabuleiro, um inteiro(jog) e um inteiro positivo(k), e devolve a posicao a jogar
    com base nas seguintes regras:
    "Se existir pelo menos uma posicao que permita obter uma linha propria com k
    pedras consecutivas (e ganhar o jogo), jogar numa dessas posicoes;
    Se nao, e se existir pelo menos uma posicao que impossibilite ao adversario de
    obter uma linha com k pedras consecutivas (e ganhar o jogo), jogar numa dessas
    posicoes;
    Se nao, para cada posicao livre, simular um jogo ate ao fim em que o jogador
    atual joga nessa posicao e o resto de jogadas sao determinadas assumindo que
    os dois jogadores alternadamente (o adversario e o proprio) jogam seguindo uma
    estrategia de jogo normal. Registar o resultado de cada simulacao e escolher a
    posicao que leva ao melhor resultado possivel, isto eh:
    Se existir pelo menos uma posicao/simulacao que permitiria ganhar o jogo,
    jogar numa dessas posicoes;
    Se nao, e se existir pelo menos uma posicao/simulacao que permitiria empatar o jogo, escolher uma dessas posicoes;
    Se nao, jogar numa posicao livre."
        Input: tab, jog, k
        Output: posicao a jogar
    '''
    (posicoes_livres) = obtem_posicoes_livres(tab)
    (posicoes_livres_ordenadas) = ordena_posicoes_tabuleiro(tab, posicoes_livres)
    if len(obtem_posicoes_jogador(tab, 1)) == 0 and len(obtem_posicoes_jogador(tab, -1)) == 0:
        return 1

    for pos in posicoes_livres_ordenadas:

        if verifica_k_linhas(marca_posicao(tab, pos, jog), pos, jog, k):
            return pos

        if verifica_k_linhas(marca_posicao(tab, pos, -jog), pos, -jog, k):
            return pos
        
        (res_tab_simulado) = tab_simulacao(tab, pos, jog, k)

        if res_tab_simulado[0]:
            if res_tab_simulado[1] == jog:
                return pos
            if not res_tab_simulado[0]:
                return pos
        
    return posicoes_livres_ordenadas[0]
        


def escolhe_posicao_auto(tab, jog, k, lvl):
    '''escolhe posicao auto(tab, jog, k, lvl) recebe um tabuleiro (em que o jogo nao terminou
ainda), um inteiro(jog), um inteiro positivo(k) e uma cadeia de carateres correspondente a estrategia,
e devolve a posicao escolhida automaticamente de acordo com a estrategia selecionada,
identificadas pelas cadeias de cararateres 'facil', 'normal' ou 'dificil'.
Sempre que houver mais do que uma posicao que cumpra um dos criterios definidos nas estrategias anteriores,
deve escolher a posicao mais proxima da posicao central do tabuleiro.
Ao mesmo tempo usa outras funcoes e condicoes para verificar os argumentos, levantando um erro caso
algum seja invalido.
    Input: tab, jog, k ,lvl
    Output: posicao a jogar
'''
    if not eh_tabuleiro(tab) or type(jog) != int or jog not in (-1, 1) or type(k) != int or not k > 0 or lvl not in ("facil", "normal", "dificil") or eh_fim_jogo(tab, k):
        raise ValueError("escolhe_posicao_auto: argumentos invalidos")
    if lvl == "facil":
        return modo_facil(tab, jog)
    if lvl == "normal":
        return modo_normal(tab, jog, k)
    if lvl == "dificil":
        return modo_dificil(tab, jog, k)
    

    

def jogo_mnk(cfg, jog, lvl):
    '''jogo mnk(cfg, jog, lvl) eh a funcao principal que permite jogar um jogo completo m, n, k
    de um jogador contra o computador. A funcao recebe um tuplo de tres valores inteiros
    correspondentes aos valores de configuracao do jogo m, n e k, um inteiro(jog)
    e uma cadeia de caracteres identificando a estrategia de jogo utilizada pela maquina.
    E segue as seguintes regras:
    "O jogo comeca sempre com o jogador com pedras pretas a marcar uma posicao
    livre e termina quando um dos jogadores vence ou se nao existirem posicoes livres no
    tabuleiro. A funcao mostra o resultado do jogo (VITORIA, DERROTA ou EMPATE) e devolve
    um inteiro identificando o jogador vencedor (1 para preto ou -1 para branco), ou 0 em
    caso de empate. 
        Input: cfg, jog, lvl
        Output: JOGO'''
    (m, n, k) = cfg
    tab = []
    jogador_atual = -1
    peca_bot = -(jog)
    for linha in range(m):
        tab.append([])
        for coluna in range(n):
            tab[linha].append(0)
        tab[linha] = tuple(tab[linha])
    tab = tuple(tab)
    if not eh_tabuleiro(tab) or type(cfg) != tuple or len(cfg)!=3 or not k > 0 or type(k)!=int or type(jog) != int or (jog not in (-1,1)) or lvl not in ("facil", "normal", "dificil"):
        raise ValueError("jogo_mnk: argumentos invalidos")
    print("Bem-vindo ao JOGO MNK.")
    if jog == 1:
        print("O jogador joga com 'X'.")
        print(tabuleiro_para_str(tab))
    else:
        print("O jogador joga com 'O'.")
        print(tabuleiro_para_str(tab))
    if jog == 1:
        tab = marca_posicao(tab, escolhe_posicao_manual(tab), jog)
    else:
        print(f"Turno do computador ({lvl}):")
        tab = marca_posicao(tab, escolhe_posicao_auto(tab, peca_bot, k, lvl), peca_bot)
        
    print(tabuleiro_para_str(tab))

    while not eh_fim_jogo(tab, k):
        if jogador_atual == jog:  
            tab = marca_posicao(tab, escolhe_posicao_manual(tab), jog)
        else:
            print(f"Turno do computador ({lvl}):")
            tab = marca_posicao(tab, escolhe_posicao_auto(tab, peca_bot, k, lvl), peca_bot)

        jogador_atual = -(jogador_atual)
        print(tabuleiro_para_str(tab))

    for pos in range(1, m*n+1):
        if verifica_k_linhas(tab, pos, jog, k):
            print("VITORIA")
            return jog
    
    for pos in range(1, m*n+1):
        if verifica_k_linhas(tab, pos, peca_bot, k):
            print("DERROTA")
            return -(jog)
          
    print("EMPATE")
    return 0


if __name__ == "__main__":
    print("=== Jogo m,n,k ===")
    print("Iniciando tabuleiro 3x3 com 3 em linha (Galo) contra o computador (normal)...")
    try:
        jogo_mnk((3, 3, 3), 1, "normal")
    except KeyboardInterrupt:
        print("\nJogo interrompido.")